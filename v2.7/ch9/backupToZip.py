#! python3
# backupToZip.py - Copies an entire folder and its content into
# a ZIP file whose file name increments.

import zipfile, os

def backupToZip(folder):
    # Backup the entire content of "folder" into a ZIP file.
    folder = os.path.abspath(folder)    # make sure folder is absolute

    # Figure out the the filename this code should use base on
    # what file already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the zip file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Ading files in %s...' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    print('Done.')

backupToZip('/home/mikhil/test')
