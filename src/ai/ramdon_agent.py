import random

def computer_move(board):
    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if board[x][y] == " ":
            return x,y