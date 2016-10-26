import os
import random
import time


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


class bcolors:  # colors
    PINK = '\033[95m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    ENDC = '\033[0m'


board = [
    " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8",
    " 9", "10", "11", "12", "13", "14", "15", "16"
]


def drawBoard():
    print("----------------------------")
    print("| ", board[0], " | ", board[1], " | ", board[2], " |", board[3], " |")
    print("----------------------------")
    print("| ", board[4], " | ", board[5], " | ", board[6], " |", board[7], " |")
    print("----------------------------")
    print("| ", board[8], " | ", board[9], " | ", board[10], " |", board[11], " |")
    print("----------------------------")
    print("| ", board[12], " | ", board[13], " | ", board[14], " |", board[15], " |")
    print("----------------------------")


def emptySpot(player):
    if board[player] != color1 + " X" + bcolors.ENDC and board[player] != color2 + " O" + bcolors.ENDC:
        return True


def winnerLine(player, spot1, spot2, spot3, spot4):
    global board
    if board[spot1] == player and board[spot2] == player and board[spot3] == player and board[spot4] == player:
        return True


def win(player):
    global board
    if player == color1 + " X" + bcolors.ENDC:
        color = " X"
    if player == color2 + " O" + bcolors.ENDC:
        color = " O"

    if winnerLine(player, 0, 1, 2, 3):  # horizontal
        for n, i in enumerate(board):
            if n < 4:
                board[n] = bcolors.RED + color + bcolors.ENDC
        return True
    if winnerLine(player, 4, 5, 6, 7):
        for n, i in enumerate(board):
            if 3 < n < 8:
                board[n] = bcolors.RED + color + bcolors.ENDC
        return True
    if winnerLine(player, 8, 9, 10, 11):
        for n, i in enumerate(board):
            if 7 < n < 12:
                board[n] = bcolors.RED + color + bcolors.ENDC
        return True
    if winnerLine(player, 12, 13, 14, 15):
        for n, i in enumerate(board):
            if 11 < n < 16:
                board[n] = bcolors.RED + color + bcolors.ENDC
        return True

    if winnerLine(player, 0, 4, 8, 12):  # vertical
        for n, i in enumerate(board):
            if n == 0 or n == 4 or n == 8 or n == 12:
                board[n] = bcolors.RED + color + bcolors.ENDC
        return True
    if winnerLine(player, 1, 5, 9, 13):
        for n, i in enumerate(board):
            if n == 1 or n == 5 or n == 9 or n == 13:
                    board[n] = bcolors.RED + color + bcolors.ENDC
        return True
    if winnerLine(player, 2, 6, 10, 14):
        for n, i in enumerate(board):
            if n == 2 or n == 6 or n == 10 or n == 14:
                    board[n] = bcolors.RED + color + bcolors.ENDC
        return True
    if winnerLine(player, 3, 7, 11, 15):
        for n, i in enumerate(board):
            if n == 3 or n == 7 or n == 11 or n == 15:
                    board[n] = bcolors.RED + color + bcolors.ENDC
        return True

    if winnerLine(player, 0, 5, 10, 15):  # diagonal
        for n, i in enumerate(board):
            if n == 0 or n == 5 or n == 10 or n == 15:
                    board[n] = bcolors.RED + color + bcolors.ENDC
        return True
    if winnerLine(player, 3, 6, 9, 12):
        for n, i in enumerate(board):
            if n == 3 or n == 6 or n == 9 or n == 12:
                    board[n] = bcolors.RED + color + bcolors.ENDC
        return True


def fullBoard():
    global board
    global color1
    global color2
    count = 0
    for i in range(16):
        if board[i] == color1 + " X" + bcolors.ENDC or board[i] == color2 + " O" + bcolors.ENDC:
            count = count + 1
        if count == 16:
            return True


def gameOfPlayer1():
    global name1
    global player1
    while True:
        player1 = input(name1 + ", select a spot 1-16 or press Q to quit: ")

        if player1.isdigit():
            player1 = int(player1)
            player1 = player1 - 1
            if player1 > 15:
                print("Select a spot between 1 and 16 or press Q to quit!")
            else:
                break
        else:
            if player1.lower() == "q":
                exit()
            print("Select a spot between 1 and 16 or press Q to quit!")


def gameOfPlayer2():
    global name2
    global player2
    while True:
        player2 = input(name2 + ", select a spot 1-16 or press Q to quit: ")
        if player2.isdigit():
            player2 = int(player2)
            player2 = player2 - 1
            if player2 > 15:
                print("Select a spot between 1 and 16 or press Q to quit!")
            else:
                break
        else:
            if player2.lower() == "q":
                exit()
            print("Select a spot between 1 and 16 or press Q to quit!")


def playAgain():
    while True:
        global board
        yes_or_no = input("Do you want to play again? (y or n) ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        if yes_or_no == "y":
            board = [
                " 1", " 2", " 3", " 4", " 5", " 6", " 7", " 8",
                " 9", "10", "11", "12", "13", "14", "15", "16"
            ]
            drawBoard()
            break
        else:
            exit()


def playAgainstCom():
    global name2
    if name2 == "C" or name2 == "c":
        return True

wins_name1 = 0  # number of wins of player1
wins_name2 = 0  # number of wins of player2


def numberOfWins1(name):  # player1
    global wins_name1
    wins_name1 = wins_name1 + 1
    print(name + " has " + str(wins_name1) + " win(s).")


def numberOfWins2(name):  # player2
    global wins_name2
    wins_name2 = wins_name2 + 1
    print(name + " has " + str(wins_name2) + " win(s).")


# HERE STARTS THE GAME
clearTerminal()
print("Welcome to Tic Tac Toe!")
print("Get ready for an awesome experience!", "\n")

name1 = input("Player1, what's your name? ")
if name1 == "":
    name1 = "Player1"  # if no name is given, it will be Player1
color1 = input("Choose a color: pink or yellow? (p/y) ")
if color1.lower() == "p":
    color1 = bcolors.PINK
elif color1.lower() == "y":
    color1 = bcolors.YELLOW
else:
    print("Ok, then your color will be yellow!")
    color1 = bcolors.YELLOW

name1 = color1 + name1 + bcolors.ENDC

name2 = input("Player2, what's your name? (Type in C to play against Computer!) ")
if name2 != "C" and name2 != "c":  # play against human
    if name2 == "":
        name2 = "Player2"  # if no name is given, it will be Player2
    color2 = input("Choose a color: blue or green? (b/g) ")
    if color2.lower() == "b":
        color2 = bcolors.BLUE
    elif color2.lower() == "g":
        color2 = bcolors.GREEN
    else:
        print("Ok, then your color will be blue!")
        time.sleep(1.5)
        color2 = bcolors.BLUE
    name2 = color2 + name2 + bcolors.ENDC
else:
    color2 = bcolors.BLUE

clearTerminal()

drawBoard()

if not playAgainstCom():  # play against human
    while True:
        gameOfPlayer1()
        if emptySpot(player1):
            board[player1] = color1 + " X" + bcolors.ENDC

            clearTerminal()

            drawBoard()

            if win(color1 + " X" + bcolors.ENDC):
                clearTerminal()
                drawBoard()
                print(name1 + " wins!")
                numberOfWins1(name1)
                print(name2 + " has " + str(wins_name2) + " win(s).")
                playAgain()

            if fullBoard() is True:
                print("It's a draw!")
                playAgain()

            while True and not fullBoard():
                gameOfPlayer2()
                if emptySpot(player2):
                    board[player2] = color2 + " O" + bcolors.ENDC

                    clearTerminal()

                    drawBoard()

                    if win(color2 + " O" + bcolors.ENDC):
                        clearTerminal()
                        drawBoard()
                        print(name2 + " wins!")
                        numberOfWins2(name2)
                        print(name1 + " has " + str(wins_name1) + " win(s).")
                        playAgain()

                    if fullBoard() is True:
                        print("It's a draw!")
                        playAgain()

                    break

                else:
                    print("Choose another spot!")

        else:
            print("Choose another spot!")

else:  # play against computer
    while True:
        gameOfPlayer1()
        if emptySpot(player1):
            board[player1] = color1 + " X" + bcolors.ENDC

            clearTerminal()

            drawBoard()

            if win(color1 + " X" + bcolors.ENDC):
                clearTerminal()
                drawBoard()
                print(name1 + " wins!")
                numberOfWins1(name1)
                if playAgainstCom():
                    print(color2 + "Computer" + bcolors.ENDC +
                          " has " + str(wins_name2) + " win(s).")
                else:
                    print(name2 + " has " + str(wins_name2) + " win(s).")
                playAgain()

            if fullBoard() is True:
                print("It's a draw!")
                playAgain()

            while True and not fullBoard():
                name2 = color2 + "Computer" + bcolors.ENDC
                random.seed
                player2 = random.randrange(0, 16)

                if emptySpot(player2):
                    board[player2] = color2 + " O" + bcolors.ENDC

                    clearTerminal()

                    drawBoard()

                    if win(color2 + " O" + bcolors.ENDC):
                        clearTerminal()
                        drawBoard()
                        print(name2 + " wins!")
                        numberOfWins2(name2)
                        print(name1 + " has " + str(wins_name1) + " win(s).")
                        playAgain()

                    if fullBoard() is True:
                        print("It's a draw!")
                        playAgain()

                    break

        else:
            print("Choose another spot!")
