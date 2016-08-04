def collatz(number):
    if (number % 2) == 0:
        temp = number // 2
    else:
        temp = 3 * number + 1
    print(temp)
    return temp

def collatzSequence():
    print('Enter number:')
    try:
        num = int(input())
    except ValueError:
        print('Error: You have entered a noninteger value. You must enter an integer value:')
        num = int(input())
    temp = collatz(num)
    while temp != 1:
        temp = collatz(temp)

collatzSequence()
