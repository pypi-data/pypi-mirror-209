import pandas as pd
import regex
from list_all_files_recursively import get_folder_file_complete_path
import numpy as np
from a_pandas_ex_horizontal_explode import pd_add_horizontal_explode
from a_pandas_ex_fastloc import (
    pd_add_fastloc,
)
from a_pandas_ex_df_to_string import pd_add_to_string
from getfilenuitkapython import get_filepath
from multisubprocess import multi_subprocess

pd_add_to_string()
pd_add_fastloc()
pd_add_horizontal_explode()

stringsexe = get_filepath("strings.exe")
compiledsplitregex = regex.compile(b"[\\r\\n]+(\\d+):")


def get_strings_from_all_files_in_folders(
    folders: str | list | tuple,
    allowed_extensions: str | list | tuple = (),
    maxsubfolders: int = -1,
    minimum_string_len: int = 5,
    unicode_ascii_both: str = "both",  # unicode, ascii or both
    bufsize: int = 65536,
    timeout: int = 10000000,
    max_threads: int = 5,
    timeout_check_sleep: int | float = 1,
    convert_to_string: bool = False,
) -> pd.DataFrame:
    """
    Retrieves strings from all files within the specified folders.

    Args:
        folders (str | list | tuple): Path of the folder(s) to search for files.
        allowed_extensions (str | list | tuple, optional): Allowed file extensions to consider. Defaults to () - all files are allowed.
        maxsubfolders (int, optional): Maximum number of subfolders to explore recursively. Defaults to -1 (all).
        minimum_string_len (int, optional): Minimum length of strings to consider. Defaults to 5.
        unicode_ascii_both (str, optional): Type of strings to consider - 'unicode', 'ascii', or 'both'. Defaults to 'both'.
        bufsize (int, optional): Buffer size for reading files. Defaults to 65536.
        timeout (int, optional): Timeout value for processing each file. Defaults to 10000000.
        max_threads (int, optional): Maximum number of threads for parallel processing. Defaults to 5.
        timeout_check_sleep (int | float, optional): Sleep duration between timeout checks. Defaults to 1.
        convert_to_string (bool, optional): Whether to convert the extracted strings to Unicode strings. Defaults to False.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted strings with corresponding file information.

    Note:
        This function internally calls the 'extract_strings_from_files' function to process individual files.
    """
    if isinstance(allowed_extensions, str):
        allowed_extensions = [allowed_extensions]
    if allowed_extensions:
        allowed_extensions = ["." + ex.strip(".").lower() for ex in allowed_extensions]
    allfi = get_folder_file_complete_path(folders, maxsubfolders=maxsubfolders)
    if allowed_extensions:
        allfiles = [x.path for x in allfi if x.ext.lower() in allowed_extensions]
    else:
        allfiles = [x.path for x in allfi]
    return extract_strings_from_files(
        allfiles=allfiles,
        minimum_string_len=minimum_string_len,
        unicode_ascii_both=unicode_ascii_both,
        bufsize=bufsize,
        timeout=timeout,
        max_threads=max_threads,
        timeout_check_sleep=timeout_check_sleep,
        convert_to_string=convert_to_string,
    )


def extract_strings_from_files(
    allfiles: list | str,
    minimum_string_len: int = 5,
    unicode_ascii_both: str = "both",  # unicode, ascii or both
    bufsize: int = 65536,
    timeout: int = 10000000,
    max_threads: int = 5,
    timeout_check_sleep: int | float = 1,
    convert_to_string: bool = False,
):
    """
    Extracts strings from the given files.

    Args:
        allfiles (list | str): List of file paths or a single file path to extract strings from.
        minimum_string_len (int, optional): Minimum length of strings to consider. Defaults to 5.
        unicode_ascii_both (str, optional): Type of strings to consider - 'unicode', 'ascii', or 'both'. Defaults to 'both'.
        bufsize (int, optional): Buffer size for reading files. Defaults to 65536.
        timeout (int, optional): Timeout value for processing each file. Defaults to 10000000.
        max_threads (int, optional): Maximum number of threads for parallel processing. Defaults to 5.
        timeout_check_sleep (int | float, optional): Sleep duration between timeout checks. Defaults to 1.
        convert_to_string (bool, optional): Whether to convert the extracted strings to Unicode strings. Defaults to False.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted strings with corresponding file information.

    Note:
        This function uses external tools to extract strings from files and requires additional dependencies.
    """
    if isinstance(allfiles, str):
        allfiles = [allfiles]
    addtocommand = []
    if unicode_ascii_both.lower() == "unicode":
        addtocommand.append("-u")
    elif unicode_ascii_both.lower() == "ascii":
        addtocommand.append("-a")

    allqueries = [
        [
            stringsexe,
            *addtocommand,
            "-n",
            str(minimum_string_len),
            "-accepteula",
            "-nobanner",
            "-o",
            h,
        ]
        for h in allfiles
    ]

    res = multi_subprocess(
        allqueries,
        byteinput=b"",
        shell=False,
        close_fds=False,
        start_new_session=True,
        bufsize=bufsize,
        invisible=True,
        timeout=timeout,
        max_threads=max_threads,
        timeout_check_sleep=timeout_check_sleep,
        kill_all_at_end=True,
        blockbatch=False,
    )

    results = [
        [x[0][-1], x[1]["stdoutready"]]
        for x in res.items()
        if x[1]["returncode"] == 0 and x[1]["stdoutready"].strip()
    ]
    df = pd.DataFrame(
        [
            [
                np.char.array(
                    compiledsplitregex.split(
                        b"\r\n"
                        + r[1]
                        + b"\r\n10000000000: DELDELDELDELDELDEL",  # just to make sure that every result contains something in the format we need
                    )[1:]
                ).reshape((-1, 2)),
                r[0],
            ]
            for r in results
        ]
    ).explode(0)
    df = pd.concat(
        [df.ds_horizontal_explode(0, False), df[1]], ignore_index=True, axis=1
    ).reset_index()
    df[0] = df[0].__array__().astype("S")
    df[1] = df[1].__array__().astype("S")
    df = df.loc[
        ~(
            df[0]
            .s_str()
            .contains(
                b"100000000", regex=False, na=False
            )  # delete the "just-to-make-sure" stuff
            & df[1].s_str().contains(b" DELDELDELDELDELD", regex=False, na=False)
        )
    ].reset_index(drop=True)
    df[0] = df[0].__array__().astype(np.uint64)
    df.columns = ["aa_fileindex", "aa_offset", "aa_string", "aa_file"]
    if convert_to_string:
        df["aa_string"] = np.char.array(df.aa_string.__array__()).decode(
            "utf-8", "ignore"
        )
    df.aa_file = df.aa_file.ds_to_string()
    return df
