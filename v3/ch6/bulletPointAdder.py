#! python3
# bulletPointAdder.py - Add Wikipedia bulletpoints to the start 
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

# seperate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):     # loop through all the indexes in the "lines" list.
    lines[i] = '* ' + lines[i]  # add star to each line in the "lines" list.

text = '\n'.join(lines)
pyperclip.copy(text)
