# devtry
![](source/devtry.png)<br>
Some pipeline automation tools.
----
## Maya
### Maya utils
- `maya_file_utils.py` : Maya file utility
    - `openPWD()` : Open current working directory (Explorer.exe)
    - `create_backup()` : Create backup file in the directory **ma_backup**
    - `up_version()` : Create a up_version of the file
        - Note: Naming convention `md_char_lou_mod_v001.mb`
- `command_line_renamer.mel` : Rename with command line.
    - `-p` : Add prefix
    - `-s` : Add suffix
    - `Sphere -p prefix -s suffix` -> RESULT: `prefix_Sphere_suffix`
- `grp.mel` : Shorthand group command.
    - `-w` : Group and make the pivot the the world center.
    - `grp "group_name" -w`
- `zero_out.mel`: Zero Out the attributes
    - `zot` : Zero out the translation
    - `zor` : Zero out the rotation
    - `zos` : Zero out the scale
    - `zo`  : Zero out translation, roation and scale
    - `zoa` : Zero out with arguments:
        - `-t` : tranlation
        - `-r` : rotation
        - `s` : scale

## devtry-cli
### devtry command line tools.
- `tx` Convert textures in to Arnold tx files. [Visit Documentation](devtry-cli/README.md)
