import random
from copy import deepcopy


def is_any_move_possible(board) -> bool:
  
  for i in range(len(board)):
    if ' ' in board[i]:
      return True

  return False
