theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    print board['top-L'] + '|' + board['top-M'] + '|' + board['top-R']
    print '-+-+-'
    print board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R']
    print '-+-+-'
    print board['low-L'] + '|' + board['low-M'] + '|' + board['low-R']

def checkBoard(board, turn):
    if board['top-L'] == turn and board['top-M'] == turn and board['top-R'] == turn:
        return True
    elif board['mid-L'] == turn and board['mid-M'] == turn and board['mid-R'] == turn:
        return True
    elif board['low-L'] == turn and board['low-M'] == turn and board['low-R'] == turn:
        return True
    elif board['top-L'] == turn and board['mid-L'] == turn and board['low-L'] == turn:
        return True
    elif board['top-M'] == turn and board['mid-M'] == turn and board['low-M'] == turn:
        return True
    elif board['top-R'] == turn and board['mid-R'] == turn and board['low-R'] == turn:
        return True
    elif board['top-L'] == turn and board['mid-M'] == turn and board['low-R'] == turn:
        return True
    elif board['top-R'] == turn and board['mid-M'] == turn and board['low-L'] == turn:
        return True
    else:
        return False

def setBoard(board, turn):
    count = 0
    while count < 9:
        printBoard(board)
        print 'Turn for ' + turn + '. Move on which space?'
        move = raw_input()
        try:
            if board[move] != ' ':
                print 'Sorry, the space is already turned'
                continue
            else:
                board[move] = turn
        except KeyError:
            print 'Inavlid key.'
            continue

        result = checkBoard(board, turn)
        if result:
            printBoard(board)
            print 'Yipee. The player ' + turn + ' have won.'
            break

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        count += 1

    if not checkBoard(board, 'X') and not checkBoard(board, 'O') and count == 9:
        printBoard(board)
        print 'Game draw, nobody won.'

def game(board):
    turn = 'X'
    setBoard(board, turn)

game(theBoard)
