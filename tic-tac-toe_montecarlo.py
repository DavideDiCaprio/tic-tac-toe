import random
from copy import deepcopy


def simulate_game(board,next_player_symbol):
    
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
    list_of_outcomes.append(simulate_game(board = deepcopy(board),next_player_symbol=next_player_symbol))
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

    
def get_available_coordinates(board):
  available_coordinates = []
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == " ":
        available_coordinates.append((i,j))

  return available_coordinates


def pick_best_move(board, player_symbol,n_simulations):

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

    if  frequency_of_wins > best_chance:
      best_chance =  frequency_of_wins
      best_move_idx = i
      
  return list_of_possible_moves[best_move_idx]


def is_any_move_possible(board) -> bool:
  
  for i in range(len(board)):
    if ' ' in board[i]:
      return True

  return False


def check_horizontal_win(board):

  for i in range(len(board)):
    if board[i] == ["O","O","O"]:
      return "O"
    elif board[i] == ["X","X","X"]:
      return "X"
      
  return None 


def check_vertical_win(board):
  
  if board[0][0] == "X" and board[1][0]== "X" and board[2][0] =="X":
    return "X"
      
  elif board[0][1] == "X" and board[1][1]== "X" and board[2][1] =="X":
    return "X"
    
  elif board[0][2] == "X" and board[1][2]== "X" and board[2][2] =="X":
    return "X"

  elif board[0][0] == "O" and board[1][0]== "O" and board[2][0] =="O":
    return "O"
      
  elif board[0][1] == "O" and board[1][1]== "O" and board[2][1] =="O":
    return "O"
    
  elif board[0][2] == "O" and board[1][2]== "O" and board[2][2] =="O":
    return "O"

  return None


def check_diagonal_win(board):
  
  if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
    return "X"
    
  elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
    return "X"

  elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
    return "O"
    
  elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
    return "O"

  return None


def get_winner(board):

  if check_horizontal_win(board) == "X" or check_horizontal_win(board) == "O":
    return check_horizontal_win(board)

  elif check_diagonal_win(board) == "X" or check_diagonal_win(board) == "O":
    return check_diagonal_win(board)

  elif check_vertical_win(board) == "X" or check_vertical_win(board) == "O":
    return check_vertical_win(board)


  else :
    return None


def get_move_coordinates(board):

  while True:
    
    coordinate_x = input("Enter coordinate x:")
    coordinate_y = input("Enter coordinate y:")
    
    allowed_input = ["0","1","2"]

    if coordinate_x in allowed_input and coordinate_y in allowed_input:
      coordinate_x = int(coordinate_x)
      coordinate_y = int(coordinate_y)
      if board[coordinate_x][coordinate_y] == " ":
        return coordinate_x,coordinate_y
        
      else : 
        print("Already taken!")

    else:
      print("Wrong coordinate.Please enter a coordinate between 0 and 2 :) ")


def print_board(board, n_spaces_offset=25):
  offset = ' '*n_spaces_offset
  print()
  print(offset+f' {board[0][0]} | {board[0][1]} | {board[0][2]}')
  print(offset+'_'*11)
  print(offset+f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
  print(offset+'_'*11)
  print(offset+f' {board[2][0]} | {board[2][1]} | {board[2][2]}')
  print()


def computer_move(board):
  
  while True:
    x = random.randint(0,2)
    y = random.randint(0,2)

    if board[x][y] == " ":
      return x,y


def play_game(user_selected_challange_level):
  
  challange_level = {
      "Beginner": 5,
      "Intermediate" : 20,
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
      x,y = pick_best_move(board=board,player_symbol=player,n_simulations=challange_level[user_selected_challange_level])
      board[x][y] = computer
      print_board(board)

  winner = get_winner(board)
  
  if winner == player:
    print('You win!') 
     
  elif winner == computer:
    print('I win!')
     
  else :
    if winner == None:
      print('The match ends in a Draw!')


def tic_tac_toe():
    
    user_selected_challange_level = input("Select challange level : Beginner, Intermediate, Advanced.")
    
    while True:
        print()
        print('*_ '*10+'NEW MATCH'+' _*'*10)
        print()
        play_game(user_selected_challange_level=user_selected_challange_level)
    
tic_tac_toe()
