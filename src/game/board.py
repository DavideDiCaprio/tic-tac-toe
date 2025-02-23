def print_board(board, n_spaces_offset=25):
    offset = ' '*n_spaces_offset
    print()
    print(offset+f' {board[0][0]} | {board[0][1]} | {board[0][2]}')
    print(offset+'_'*11)
    print(offset+f' {board[1][0]} | {board[1][1]} | {board[1][2]}')
    print(offset+'_'*11)
    print(offset+f' {board[2][0]} | {board[2][1]} | {board[2][2]}')
    print()

def is_any_move_possible(board) -> bool:
    for i in range(len(board)):
        if ' ' in board[i]:
            return True
    return False

def get_available_coordinates(board):
    available_coordinates = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                available_coordinates.append((i,j))
    return available_coordinates