# This program checks whether if you are Alice or not, and also if you are a little kid or not

print('What is your name?')
name = input()
print('How old are you?')
age = int(input())

if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice, nor a little kid.')
