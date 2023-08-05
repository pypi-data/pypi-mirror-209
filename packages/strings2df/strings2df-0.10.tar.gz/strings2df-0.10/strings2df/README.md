# Results of strings.exe to pandas DataFrame 

## pip install strings2df

### Tested against Windows 10 / Python 3.10 / Anaconda


The utility leverages multiprocessing techniques to extract strings from files concurrently (with Microsoft's strings.exe), utilizing the available system resources efficiently. 

It can handle large volumes of files or folders with configurable parameters, such as buffer size and maximum threads, ensuring optimal performance.

Users have the flexibility to extract strings from individual files or entire folders by specifying the desired file paths or folder paths. They can also define additional criteria, such as allowed file extensions or minimum string length, to filter the extracted strings.

The extracted strings are returned as a pandas DataFrame, a powerful data manipulation tool. Users can apply various pandas functions to filter, transform, or analyze the extracted strings, enabling in-depth exploration and further processing.

Unicode and ASCII Support: The utility provides options to extract either Unicode strings, ASCII strings, or both, allowing users to handle different types of text data present in files accurately.

By combining efficiency, flexibility, and data manipulation capabilities, this utility simplifies the process of extracting strings from files, empowering users to derive valuable insights from text data efficiently.

Please note that the provided information is for illustrative purposes only, and the utility's usefulness may vary depending on specific use cases and requirements.


### To extract strings from individual files:

```python

from strings2df import extract_strings_from_files
df = extract_strings_from_files(
    allfiles=[
        r"C:\Users\hansc\Desktop\create_new_anaconda_env - Copy.bat",
        r"C:\cygwinxx\bin\etags.exe",
        r"C:\cygwinxx\bin\apt",
    ],
    minimum_string_len=5,
    unicode_ascii_both="both",
    bufsize=100000,
    timeout=1000000,
    max_threads=5,
    timeout_check_sleep=1,
    convert_to_string=False,
)
# print(df[:5].to_string())
#    aa_fileindex  aa_offset                                                                aa_string              aa_file
# 0             0          0                                                           b'#!/bin/bash'  C:\cygwinxx\bin\apt
# 1             0         12  b'        # apt-cyg: install tool for Cygwin similar to debian apt-get'  C:\cygwinxx\bin\apt
# 2             0         81                                                             b'        #'  C:\cygwinxx\bin\apt
# 3             0         91                                       b'        # The MIT License (MIT)'  C:\cygwinxx\bin\apt
# 4             0        123                                                             b'        #'  C:\cygwinxx\bin\apt
```

### To extract strings from files within folders:


```python

from strings2df import get_strings_from_all_files_in_folders

df2 = get_strings_from_all_files_in_folders(
    folders=[
        r"C:\ProgramData\BlueStacks_nxt",
    ],
    allowed_extensions=(".exe", ".cfg"),
    maxsubfolders=-1,
    minimum_string_len=5,
    unicode_ascii_both="both",
    bufsize=100000,
    timeout=1000000,
    max_threads=5,
    timeout_check_sleep=1,
    convert_to_string=True,
)
# print(df2[:5].to_string())
#    aa_fileindex  aa_offset                                   aa_string                                                         aa_file
# 0             0          0  DesktopShortcutFileName = BlueStacks 5.lnk  C:\ProgramData\BlueStacks_nxt\Engine\Nougat64\oem_Nougat64.cfg
# 1             0         43      ControlPanelDisplayName = BlueStacks 5  C:\ProgramData\BlueStacks_nxt\Engine\Nougat64\oem_Nougat64.cfg
# 2             0         82             IsPixelParityToBeIgnored = true  C:\ProgramData\BlueStacks_nxt\Engine\Nougat64\oem_Nougat64.cfg
# 3             0        114                                   OEM = nxt  C:\ProgramData\BlueStacks_nxt\Engine\Nougat64\oem_Nougat64.cfg
# 4             0        124           IsCreateDesktopIconForApp = false  C:\ProgramData\BlueStacks_nxt\Engine\Nougat64\oem_Nougat64.cfg

# The extracted strings will be returned as a pandas DataFrame (df in the above examples) with columns representing the file index, offset, string, and file path.

# You can manipulate and filter the DataFrame using pandas functions. For example:


# You can work with binaries like with strings:
# Just use Series.s_str() # included in this module - https://github.com/hansalemaos/a_pandas_ex_fastloc
# df.loc[df.aa_string.s_str().contains(b'xml',regex=True, flags=regex.I)]
```



