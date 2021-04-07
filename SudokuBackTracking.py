grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

def sudoku_valid(grid, n, pos):

    #Checking if any element in row is repeated
    for i in range(9):
        if(grid[pos[0]][i]==n and pos[1]!=i):
            return False

    # Checking if any element in Column is repeated
    for i in range(9):
        if (grid[i][pos[1]] == n and pos[0] != i):
                return False

    # Checking the Box
    x_box = pos[1] // 3
    y_box = pos[0] // 3

    for i in range(y_box*3, y_box*3+3):
        for j in range(x_box*3, x_box*3+3):
            if(grid[i][j] == n and (i, j) != pos):
                return False
    return True

def solve(grid):
    find = find_empty(grid)
    if(not find):
        return True
    else:
        row, col = find_empty(grid)

    for i in range(1, 10):
        if sudoku_valid(grid, i, (row, col)):
            grid[row][col] = i
            if solve(grid):
                return True
            grid[row][col] = 0

    return False

def print_sudoku(grid):

    for i in range(len(grid)):
        if(i%3 == 0 and i != 0):
            print("- - - - - - - - - - - ")
        for j in range(len(grid[i])):
            if(j%3 == 0 and j != 0):
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()

#print_sudoku(grid)

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if(grid[i][j] == 0):
                return (i, j)
    return None

#print(find_empty(grid))

print("Visual representation of the unsolved Sudoku puzzle:\n")
print_sudoku(grid)
solve(grid)
print("\nThe solved Puzzle is: \n")
print_sudoku(grid)