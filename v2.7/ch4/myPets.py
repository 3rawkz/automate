myPets = ['Zophie', 'Pooka', 'Fat-tail']
print 'Enter a pet name:'
name = raw_input()
if name not in myPets:
    print 'I do not have pet named ' + name
else:
    print name + ' is my pet'
