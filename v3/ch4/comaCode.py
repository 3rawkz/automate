def comaCode(l):
    string = ''
    for i in range(len(l)):
        if type(l[i]) != 'str':
            t1 = str(l[i])
        else:
            t1 = l[i]

        if i < len(l)-1:
            t2 = t1 + ', '
        else:
            t2 = 'and ' + t1

        string += t2

    return string

spam = ['apples', 'banana', 'tofu', 'cats', 2, 6]
print('The given list :')
print(spam)
print('After passing list to the comaCode function, the list \
becomes : ')
print(comaCode(spam))
