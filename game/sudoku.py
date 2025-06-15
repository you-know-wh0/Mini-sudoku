import random

# Initialize an empty 9x9 grid
def create_empty_grid():
    return [[0 for _ in range(9)] for _ in range(9)]

# Check if a number is valid in a given position
def is_valid(grid, row, col, num):
    # Check row 
    if num in grid[row]:
        return False
    
    # Check column
    if num in [grid[i][col] for i in range(9)]:
        return False
    
    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if grid[i][j] == num:
                return False
    
    return True

# Solve the Sudoku puzzle using backtracking
def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Generate a solved Sudoku puzzle
def generate_solved_grid():
    grid = create_empty_grid()
    solve(grid)
    return grid

# Create a puzzle by removing some numbers
def create_puzzle(solved_grid, difficulty):
    puzzle = [row[:] for row in solved_grid]
    cells_to_remove = difficulty
    while cells_to_remove > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            cells_to_remove -= 1
    return puzzle

# Print the Sudoku grid
def print_grid(grid):
    for i, row in enumerate(grid):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j, num in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(num if num != 0 else ".", end=" ")
        print()

# Main game loop
def play_sudoku():
    print("Welcome to Sudoku!")
    difficulty = int(input("Enter difficulty (number of empty cells, 20-60): "))
    
    solved_grid = generate_solved_grid()
    puzzle = create_puzzle(solved_grid, difficulty)
    
    while True:
        print_grid(puzzle)
        
        row = int(input("Enter row (1-9): ")) - 1
        col = int(input("Enter column (1-9): ")) - 1
        num = int(input("Enter number (1-9): "))
        
        if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
            if puzzle[row][col] == 0:
                if solved_grid[row][col] == num:
                    puzzle[row][col] = num
                    if puzzle == solved_grid:
                        print("Congratulations! You've solved the puzzle!")
                        break
                else:
                    print("Incorrect number. Try again.")
            else:
                print("This cell is already filled. Try another one.")
        else:
            print("Invalid input. Try again.")
play_sudoku()