import random
from ..game.board import print_board, is_any_move_possible
from ..game.win_checker import get_winner
from ..ai.random_agent import computer_move


def play_singleplayer():
    board = ([" "," "," "],[" "," "," "],[" "," "," "])

    player = input("Hi Player. Select X or O: ")
    while player not in ['O', 'X']:
        print('You must pick either X or O !')
        player = input("Hi player. Select X or O: ")
        
    computer = 'X' if player == 'O' else 'O' 

    print_board(board)

    while get_winner(board) == None and is_any_move_possible(board):
        print("Player is your turn...")
        x,y = get_move_coordinates(board)
        board[x][y] = player
        print_board(board)

        if get_winner(board) == None and is_any_move_possible(board):
            print("My turn....")
            x,y = computer_move(board)
            board[x][y] = computer
            print_board(board)

    winner = get_winner(board)
    
    if winner == player:
        print('You win!') 
    elif winner == computer:
        print('I win!')
    else:
        if winner == None:
            print('The match ends in a Draw!')

def get_move_coordinates(board):
    while True:
        coordinate_x = int(input("Enter coordinate x:"))
        coordinate_y = int(input("Enter coordinate y:"))

        if coordinate_x >= 0 and coordinate_x <3 and coordinate_y >= 0 and coordinate_y <3:
            if board[coordinate_x][coordinate_y] == " ":
                return coordinate_x,coordinate_y
            else: 
                print("Already taken!")
        else:
            print("Wrong coordinate.Please enter a coordinate between 0 and 2 :) ")