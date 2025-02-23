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
            else: 
                print("Already taken!")
        else:
            print("Wrong coordinate.Please enter a coordinate between 0 and 2 :) ")