#! python3
# regexSearch.py - Python program that opens all '.txt' files in a folder and searches for any
# line that matches a user-supplied regular expression. The results should be printed to the screen.

import os, sys, re

def text_file_search(path):
    abs_path = os.path.abspath(path)
    items = os.listdir(abs_path)
    text_files = []
    for item in items:
        text_match = re.match(r'\w+.txt', item)
        if text_match:
            text_files.append(item)
    return text_files

def regex_search(path, pattern):
    txt_list = text_file_search(path)
    for item in txt_list:
        txt_file = open(item, 'r')
        print('\n' + ' ' * 20 + item + '\n-----------------------------------------------------------\n')
        line = txt_file.readline()
        while line:
            m = re.match(pattern, line)
            if m:
                print(line)
            line = txt_file.readline()
        print('\n')

def main():
    if len(sys.argv) != 2:
        print('INVALID ENTRY.')
        sys.exit(1)
    path = sys.argv[1]
    pattern = input('Enter a regular expression to search : ')
    regex_search(path, pattern)

if __name__ == '__main__':
    main()
