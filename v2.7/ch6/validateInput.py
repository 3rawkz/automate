while True:
    print 'Enter your age:'
    age = raw_input()
    if age.isdigit():
        break
    print 'Please enter a number for your age.'

while True:
    print 'Select a new password (letters and passwords only):'
    password = raw_input()
    if password.isalnum():
        break
    print 'Passwords can only have letters and numbers.'
