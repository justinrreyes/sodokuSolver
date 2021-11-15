board = [
    [8, 0, 5, 0, 9, 7, 1, 0, 0],
    [0, 4, 2, 0, 1, 6, 0, 0, 7],
    [7, 1, 0, 3, 0, 8, 4, 0, 5],
    [1, 7, 8, 2, 0, 0, 6, 5, 0],
    [5, 9, 4, 6, 0, 1, 7, 0, 3],
    [0, 0, 6, 7, 4, 5, 0, 0, 1],
    [0, 0, 7, 0, 0, 4, 0, 0, 8],
    [9, 8, 3, 1, 7, 0, 0, 0, 0],
    [4, 0, 1, 8, 6, 0, 2, 0, 9]
]

def solve(board):

    find = findEmpty(board) #checks for empty spaces, if not, board is solved
    if not find:
        return True
    else:
        row, col = find
    #Finds a valid number for the empty space
    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i #Once found adds number to the board

            if solve(board): #Recursion to determine if the board is completely filled/solved
                return True

            board[row][col] = 0 # backtracks, sets previous space to 0, trys new number

    return False
    

def valid(board, num, pos): # determines if number is valid in its space
    for i in range(len(board[0])): #Checks if number is in row or column
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y*3 + 3):  #Checks if number is in "box"
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def printBoard(board): #prints board formatted

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="") 



def findEmpty(board): # finds an empty space in the board, looks for a 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

printBoard(board) #unsolved board
solve(board) #solves board
print("____________________________") #divider for clarity
printBoard(board) #prints solved board