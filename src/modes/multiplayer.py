from src.game.board import print_board, is_any_move_possible
from src.game.win_checker import get_winner


def play_multiplayer():
    board = ([" "," "," "],[" "," "," "],[" "," "," "])

    player1 = input("Hi Player 1. Select X or O: ")
    while player1 not in ['O', 'X']:
        print('You must pick either X or O !')
        player1 = input("Hi player. Select X or O: ")
        
    player2 = 'X' if player1 == 'O' else 'O' 
    
    print_board(board)

    while get_winner(board) == None and is_any_move_possible(board):
        print("Player 1 is your turn...")
        x,y = get_move_coordinates(board)
        board[x][y] = player1
        print_board(board)

        if get_winner(board) == None and is_any_move_possible(board):
            print("Player 2 is your turn...")
            x,y = get_move_coordinates(board)
            board[x][y] = player2
            print_board(board)

    winner = get_winner(board)
    win_msg = f'Player {winner} wins!' if winner is not None else 'The match ends in a Draw!'
    print(win_msg)

    return winner

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