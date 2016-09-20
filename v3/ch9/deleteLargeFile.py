#! python3
# deleteLargeFile.py - Delete bulk files (files with size more than 100MB).

import shutil, os, send2trash, sys

def deleteLargeFile(folder):
    folder = os.path.abspath(folder)
    files = os.listdir(folder)

    print(files)
    for item in files:
        size = os.path.getsize(os.path.abspath(os.path.join(folder, item)))
        if size >= 104857600:
            file_path = os.path.abspath(os.path.join(folder, item))
            print(file_path) 
            # shutil.unlink(file_path)
            # send2trash.send2trash(file_path)

def main():
    if len(sys.argv) != 2:
        print('ERROR......!!!!!!')
        sys.exit(1)
    folder = sys.argv[1]
    deleteLargeFile(folder)

main()
