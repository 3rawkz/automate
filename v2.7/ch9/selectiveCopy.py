#! python3
# selectiveCopy.py - Python script that walks through a folder tree and searches 
# for files with a certain file extension (such as .pdf or .jpg). Copy these files
# from whatever location they are in to a new folder.

import shutil, os, sys

def selectiveCopy(folder, file_type):
    folder = os.path.abspath(folder)    # make sure folder is absolute
    dest_folder = file_type + '_folder'
    os.chdir(folder)
    if not os.path.exists(dest_folder):
        os.mkdir(os.path.join(folder, dest_folder))
    dest_folder = os.path.abspath(dest_folder)

    for foldername, subfolders, filenames in os.walk(folder):
        print 'Checking %s..\n' % (foldername)

        for filename in filenames:
            name = filename.lower()
            t = file_type.upper()
            if name.endswith(file_type) or filename.endswith(t):
                shutil.copy(os.path.join(folder, filename), dest_folder)
    print 'Done.'

def main():
    if len(sys.argv) != 2:
        print 'Folder not specified!'
        sys.exit(1)
    folder = sys.argv[1]
    file_type = raw_input('Enter the file type to copy : ')
    selectiveCopy(folder, file_type)

main()
