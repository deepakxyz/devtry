# devtry
![](source/devtry.png)<br>
Some pipeline automation tools.
----
## Maya
- `maya_file_utils.py` : Maya file utility
    - `openPWD()` : Open current working directory (Explorer.exe)
    - `create_backup()` : Create backup file in the directory **ma_backup**
    - `up_version()` : Create a up_version of the file
        - Note: Naming convention `md_char_lou_mod_v001.mb`
- `command_line_renamer.py` : Rename with command line.
    - `-p` : Add prefix
    - `-s` : Add suffix
    - `Sphere -p prefix -s suffix` -> RESULT: `prefix_Sphere_suffix`

