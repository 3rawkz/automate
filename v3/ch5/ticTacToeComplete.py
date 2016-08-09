#! python 3
# ticTacToeComplete.py - This program is used for playing the game TIC-TAC-TOE.

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
# theBoard is a dictionary. This dictionary is used for representing the data structure for this game.

import sys

def printBoard(board):
    # this function prints the current status of the tic-tac-toe board in graphics mode.
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

def checkBoard(board, turn):
    # this function checks whether the game won or not. If the return value is True, then game won, otherwise not won.
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
        print('Turn for ' + turn + '. Move on which space?')
        move = input()
        try:
            # this try block check for KeyError
            if board[move] != ' ':
                print('Sorry, the space is already turned')
                continue
            else:
                board[move] = turn
        except KeyError:
            print('Inavlid key.')
            continue

        result = checkBoard(board, turn)
        if result:
            # if the variable result is True, then game won.
            printBoard(board)
            print('Yipee. The player ' + turn + ' have won.')          
            break

        # switching the turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

        count += 1

    if not checkBoard(board, 'X') and not checkBoard(board, 'O') and count == 9:
        # If either X or O haven't won and number of chances is exceeded the limit.
        printBoard(board)
        print('Game draw, nobody won.')

def game(board):
    print('Who wants to start first? (X or O)')
    turn = input()
    if turn == 'X' or turn == 'x':
        setBoard(board, 'X')
    elif turn == 'O' or turn == 'o':
        setBoard(board, 'O')
    else:
        print('Wrong choice.')
        sys.exit()

game(theBoard)
