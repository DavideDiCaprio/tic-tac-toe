import random
from copy import deepcopy

def simulate_game(board, next_player_symbol):
    from src.game.win_checker import get_winner
    from src.game.board import is_any_move_possible
    from src.ai.random_agent import computer_move
    
    while get_winner(board) == None and is_any_move_possible(board):
        x,y = computer_move(board)
        board[x][y] = next_player_symbol

        if get_winner(board) == None and is_any_move_possible(board):
            x,y = computer_move(board)
            board[x][y] = next_player_symbol

    winner = get_winner(board)
    return winner

def simulate_game_n_times(n_times, board, next_player_symbol):
    list_of_outcomes = []
    while len(list_of_outcomes) != n_times:
        list_of_outcomes.append(simulate_game(board=deepcopy(board), next_player_symbol=next_player_symbol))
    return list_of_outcomes

def measure_frequency_of_outcome(outcome, list_of_outcomes):
    count = 0
    frequency = 0
    for i in range(len(list_of_outcomes)):
        if outcome == list_of_outcomes[i]:
            count+=1
            frequency = count/len(list_of_outcomes)
    return frequency

def measure_frequency_of_outcomes(list_of_outcomes):
    observed_outcomes = list(set(list_of_outcomes)) 
    for o in observed_outcomes:
        measure_frequency_of_outcome(outcome=o, list_of_outcomes=list_of_outcomes)

def pick_best_move(board, player_symbol, n_simulations):
    from src.game.board import get_available_coordinates
    
    list_of_possible_moves = get_available_coordinates(board=board)
    odds_of_winning_per_each_move = []
    best_chance = 0
    next_player_symbol = "O"
    best_move_idx = 0

    if player_symbol == "O":
        next_player_symbol = "X"
        
    for i in range(len(list_of_possible_moves)):
        candidate_board = deepcopy(board)
        x,y = list_of_possible_moves[i]
        candidate_board[x][y] = player_symbol

        simulated_outcomes = simulate_game_n_times(n_times=n_simulations, board=candidate_board, next_player_symbol=next_player_symbol)
        frequency_of_wins = measure_frequency_of_outcome(outcome=player_symbol, list_of_outcomes=simulated_outcomes)
        odds_of_winning_per_each_move.append(frequency_of_wins)

        if frequency_of_wins > best_chance:
            best_chance = frequency_of_wins
            best_move_idx = i
            
    return list_of_possible_moves[best_move_idx]