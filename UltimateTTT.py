board = [[' ' for x in range(9)] for y in range(9)]
winner = [' ' for x in range(9)]
pieces = ['x', 'o']


def clear():
    print('\n' * 50)


def emptyLine():  # only used for printBoard()
    print('\n|           |           |           |')


def printBoard():
    print('-------------------------------------')
    for y in range(3):
        for x in range(3):
            print('| ' + board[y * 3 + x][0] + '   ' + board[y * 3 + x][1] + '   ' + board[y * 3 + x][2] + ' ', end='')
        print('|', end='')
        emptyLine()
        for x in range(3):
            print('| ' + board[y * 3 + x][3] + '   ' + board[y * 3 + x][4] + '   ' + board[y * 3 + x][5] + ' ', end='')
        print('|', end='')
        emptyLine()
        for x in range(3):
            print('| ' + board[y * 3 + x][6] + '   ' + board[y * 3 + x][7] + '   ' + board[y * 3 + x][8] + ' ', end='')
        print('|\n-------------------------------------')
    print('\n')


def playerMove(location, piece):
    if location >= 0:
        while True:
            move = input("Select a position to place an 'x' from 1 - 9: ")
            try:
                move = int(move)
                if move > 0 and move < 10:
                    if board[location][move - 1] == ' ':
                        board[location][move - 1] = piece
                        break
            except TypeError:
                pass
    else:
        while True:
            location = input("Select a new box to place an 'x' from 1 - 9: ")
            try:
                location = int(location) - 1
                if winner[location] == ' ':
                    break
            except TypeError:
                pass
        while True:
            move = input("Select a position in the box to place an 'x' from 1 - 9: ")
            try:
                location = int(location)
                move = int(move)
                if move > 0 and move < 10:
                    if board[location][move - 1] == ' ':
                        board[location][move - 1] = piece
                        break
            except TypeError:
                pass
    return (move - 1)


def winSmallBox(location, piece):
    for x in range(0, 9, 3):
        if (board[location][x] == board[location][x + 1] and board[location][x] == board[location][x + 2] and board[location][x] == piece):
            return True
    for x in range(0, 3):
        if (board[location][x] == board[location][x + 3] and board[location][x] == board[location][x + 6] and board[location][x] == piece):
            return True
    if (board[location][0] == board[location][4] and board[location][0] == board[location][8] and board[location][0] == piece):
        return True
    elif (board[location][2] == board[location][4] and board[location][2] == board[location][6] and board[location][2] == piece):
        return True
    return False


def isWinner(piece):
    for x in range(0, 9, 3):
        if (winner[x] == winner[x + 1] and winner[x] == winner[x + 2] and winner[x] == piece):
            return True
    for x in range(0, 3):
        if (winner[x] == winner[x + 3] and winner[x] == winner[x + 6] and winner[x] == piece):
            return True
    if (winner[0] == winner[4] and winner[0] == winner[8] and winner[0] == piece):
        return True
    elif (winner[2] == winner[4] and winner[2] == winner[6] and winner[2] == piece):
        return True
    return False


def isBoardFull(boardNum):
    if board[boardNum].count(' ') == 0:
        return True
    return False


def isEntireBoardFull():
    for x in range(9):
        if not isBoardFull(x):
            return False
    return True


def main():
    move = 0
    FIRST_LOCATION = 4
    location = FIRST_LOCATION
    clear()
    print('Welcome to Ultimate Tic Tac Toe')
    printBoard()

    while not (isEntireBoardFull()):
        hasWon = 0
        nextLocation = playerMove(location, pieces[move])
        if(winSmallBox(location, pieces[move])):
            winner[location] = pieces[move]
            location = -1
            if isWinner(pieces[move]):
                printBoard()
                print("Congrats! Player {} won the game".format(move + 1))
                hasWon += 1
                break
        elif(isBoardFull(location)):
            winner[location] = 'T'
            if (winner[nextLocation] == ' '):
                location = nextLocation
            else:
                location = -1
        else:
            if (winner[nextLocation] == ' '):
                location = nextLocation
            else:
                location = -1

        move = (move + 1) % 2
        printBoard()
        print(winner)

    if isEntireBoardFull() and hasWon == 0:
        print('Tie Game')


main()
