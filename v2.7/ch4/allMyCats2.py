catNames = []
while True:
    print 'Enter the name of the cat ' + str(len(catNames) + 1) + '(Or enter nothing to stop.) :'
    name = raw_input()
    if name == '':
        break
    catNames = catNames + [name]
print 'The cat names are :'
for name in catNames:
    print ' ' + name
