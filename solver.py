def valid_board(board, num, pos):
    for row in range(len(board[0])):
        if board[pos[0]][row] == num and pos[1] != row:
            return False
    
    for col in range(len(board)):
        if board[col][pos[1]] == num and pos[0] != col:
            return False
        
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for row in range(box_y * 3, box_y * 3 + 3):
        for col in range(box_x * 3, box_x * 3 + 3):
            if board[row][col] == num and (row, col) != pos:
                return False
            
    return True

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
            
    return None

def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - ")

        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")

