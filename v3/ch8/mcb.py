#! python3
# mcb.py - Saves and loads pieces of texts to the clipboard to keyword.
# Usage: python3 mcb.py save <keyword> - Saves clipboard to keyword.
#        python3 mcb.py <keyword> - Loads keyword to clipboard.
#        python3 mcb.py list - Loads all keywords to clipboard.

import shelve, pyperclip, sys, pprint

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    if sys.argv[2].lower() == 'all':
        for key in mcbShelf.keys():
            del mcbShelf[key]
    else:
        del mcbShelf[sys.argv[2].lower()]
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    pprint.pprint(pyperclip.paste())

mcbShelf.close()
