import sys
import os
from .txmake import txmake, test

HELP_CMD = '''
tx --help -h                List all the available commands
tx run                      Convert all the texture to to tx
'''

def main():
    args = sys.argv[1:]
    try:
        if args[0] == "test":
            print("This is working")
        if args[0] == "cwd":
            print(os.getcwd()) 

        # main command
        if args[0] == "run":
            # argument flags 
            # -t : Type of file
            try:
                if args[1] == "-t" or args[1] == "--type" and len(args[2]) > 0: 
                    # check if args[2] exists
                    if args[2] in ['.exr','.jpg','.png','tif']:
                        print("Running on only "+ args[2] + " files")
                        txmake(type=args[2])
                    else:
                        print("Unknown file format",args[2])
                
            except:
                print("Running over all files")
                txmake()
        
        if args[0] == "--help" or args[0] == "-h":
            print(HELP_CMD)

                
    except:
        print("No command found.")

if __name__ == '__main__':
    main()
