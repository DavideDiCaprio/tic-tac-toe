#my version of tic tac toe game


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

  
def print_board(board, n_spaces_offset=25):
  offset = ' '*n_spaces_offset
  print()
  print(offset+f' {board[0][0]} | {board[0][1]} | {board[0][2]}')
  print(offset+'_'*11)
  print(offset+f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
  print(offset+'_'*11)
  print(offset+f' {board[2][0]} | {board[2][1]} | {board[2][2]}')
  print()
  
def play_game():

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


def tic_tac_toe():
  while True:
    print()
    print('*_ '*10+'NEW MATCH'+' _*'*10)
    print()
    play_game()
    
tic_tac_toe()
