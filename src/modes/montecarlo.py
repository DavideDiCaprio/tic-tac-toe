from src.game.board import print_board, is_any_move_possible
from src.game.win_checker import get_winner
from src.game.player import get_move_coordinates
from src.ai.monte_carlo import pick_best_move

def play_game(user_selected_challenge_level):
    challenge_level = {
        "Beginner": 5,
        "Intermediate": 20,
        "Advanced": 1000
    }
    
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
            x,y = pick_best_move(board=board, player_symbol=computer, n_simulations=challenge_level[user_selected_challenge_level])
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

def tic_tac_toe():
    user_selected_challenge_level = input("Select challange level : Beginner, Intermediate, Advanced.")
    
    while True:
        print()
        print('*_ '*10+'NEW MATCH'+' _*'*10)
        print()
        play_game(user_selected_challenge_level=user_selected_challenge_level)

if __name__ == "__main__":
    tic_tac_toe()