# This program checks whether you are a vampire or not

print 'What is your name?'     # asks for your name
name = raw_input()
print 'How old are you?'       # asks for your age
age = int(raw_input())

if name == 'Alice':
    print 'Hi, Alice.'
elif age < 12:
    print 'You are not Alice kiddo.'
elif age > 100:
    print 'You are not Alice, grannie.'
elif age > 2000:
    print 'Unlike you, Alice is not undead, immortal vampire.'
