import os

def txmake(type=""):
    # available extension for the tx to work
    ext_list = ['.exr','.png','.jpg','.tiff']

    # get current working directory
    cwd = os.getcwd()

    # get all the files from the directory
    all_files = os.listdir(cwd)

    

    # set extension list
    if type == "":
        extensions = ext_list
    else:
        # check if the extension is valid
        int_ext = [type]
        if int_ext[0] in ext_list:
            extensions = int_ext
    
    # remove all the type of files other than the list-> fle_ext
    for file in all_files:
        raw,ext = os.path.splitext(file)
        if ext in extensions:
            image_file_path = os.path.join(cwd,raw) + ext
            tx_file_path = os.path.join(cwd,raw) + ".tx"
            maketx = f"maketx -v -u --oiio --checknan --filter lanczos3 {image_file_path} -o {tx_file_path}"
            os.system(maketx)

        

def test(type=""):
    print("hello")
