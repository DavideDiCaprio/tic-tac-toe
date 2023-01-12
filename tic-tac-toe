#my version of tic tac toe game

def is_any_move_possible(board) -> bool:
  
  for i in range(len(board)):
    if board[i][i] == " ":
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
