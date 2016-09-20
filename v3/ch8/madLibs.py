#! python3
# madLibs.py - Python script to create a Mad Libs program that reads in text files and lets the user add
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears in the text file.

import re, pprint

old_file = open('madLibs_old.txt', 'r')
old_text = old_file.read()
old = ['ADJECTIVE', 'NOUN', 'VERB', 'NOUN']

new_file = open('madLibs_new.txt', 'w')
for item in old:
    # read the replacing word.
    if item == 'ADJECTIVE' or item == 'ADVERB':
        replace = input('Enter an %s:' % (item,))
    else:
        replace = input('Enter a %s:' % (item,))

    # substitue the replacement word.
    if item == old[0]:
        new_text = re.sub(item, replace, old_text, count = 1)
    else:
        new_text = re.sub(item, replace, new_text, count = 1)

new_file.write(new_text)

old_file.close()
new_file.close()
