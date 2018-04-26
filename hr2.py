import re
import random

stepCounter = 0
board = ({1: {1:" ", 2:" ", 3:" "},
          2: {1:" ", 2:" ", 3:" "},
          3: {1:" ", 2:" ", 3:" "}})

def whosFirst():
    if random.randint(0, 1) == 0:
        return 'O'
    else:
        return 'X'

def checkEmpty(board, row, col):
    if board[row][col] == " ":
        return True
    return False

def drawBoard(board):
    print(' ' + board[1][1] + ' | ' + board[1][2] + ' | ' + board[1][3])
    print('-----------')
    print(' ' + board[2][1] + ' | ' + board[2][2] + ' | ' + board[2][3])
    print('-----------')
    print(' ' + board[3][1] + ' | ' + board[3][2] + ' | ' + board[3][3])
    


def checkRows(board):
    for key in board:
        rvals = list(set(board[key].values()))
        if len(rvals) == 1 and rvals[0] != " ":
            return "real " + str(key)
    return 0

def checkCols(board):
    for col in range (1,3):
        colum = [board[1][col], board[2][col], board[3][col]]
        cvals = list(set(colum))
        if len(cvals) == 1 and cvals[0] != " ":
            return "veerg " + str(col)
    return 0

def checkDiag(board):
    diag1 = list(set([board[1][1], board[2][2], board[3][3]]))
    diag2 = list(set([board[1][3], board[2][2], board[3][1]]))
    if len(diag1) == 1 and diag1[0] != " ":
        return "diagonaalselt ülevalt vasakult alla paremale"
    if len(diag2) == 1 and diag2[0] != " ":
        return "diagonaalselt alt vasakult ülesse paremale"
    return 0

def checkIfFull(board):
    for x in range(1, 4):
        for y in range(1, 4):
            if (checkEmpty(board, x, y)):
                return False
    return True



def checkIfkWinner(board):
    if not (checkDiag(board) == 0):
        return checkDiag(board)
    if not (checkRows(board) == 0):
        return checkRows(board)
    if not (checkCols(board) == 0):
        return checkCols(board)



turn = whosFirst()
print ("Mänguplats:")
drawBoard(board)
print("Mängujuhend: Sisesta rida ja veerg kujul RIDA-VEERG [3-2].")
while True:
    insert = input(f"Mängija {turn} kord, sisesta uus rida-veerg [1-2].")
    if len(insert) == 0:
        break
    
    stepCounter += 1

    match =  re.match('^[1-3]-[1-3]$', insert)
    row = int(insert[0])
    col = int(insert[2])
        
    if match == None:
	    print('Sisend ei vasta vormingule, palun proovi uuesti.')
    elif not(checkEmpty(board, row, col)):
	    print('See koht on juba võetud, proovi uuesti.')
    else:
        board[row][col] = turn
        drawBoard(board)

    if (checkIfkWinner(board)):
        print (f"Võitis mängija {turn}, {checkIfkWinner(board)}.")
        break
    
    if (checkIfFull(board)):
        print (f"Plats sai täis, jäite viiki.")
        break
    
    
    if turn == 'O':
        turn = 'X'
    else:
        turn = 'O'


    
