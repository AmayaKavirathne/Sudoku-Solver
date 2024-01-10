# Sudoku-Solver

This Python script provides a simple implementation of a Sudoku solver using a backtracking algorithm. The solver is capable of solving a given Sudoku puzzle and printing the solved board. The Sudoku puzzle is represented as a 9x9 grid where empty cells are denoted by the value -1.


#Functions
find_next_empty(puzzle)
This function finds the next empty cell in the Sudoku puzzle. It returns the row and column of the empty cell. If there are no empty cells, it returns None, None.

is_valid(puzzle, guess, row, col)
This function checks whether a guess at a given row and column in the puzzle is valid. It returns True if the guess is valid and False otherwise.

solve_sudoku(puzzle)
The main function for solving the Sudoku puzzle using a backtracking algorithm. It makes recursive calls to find a valid solution by trying different numbers in empty cells.


#Usage
The script includes an example Sudoku board represented as a 9x9 list. To solve the Sudoku puzzle, run the script, and it will print the solved puzzle or indicate if the puzzle is unsolvable.

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)


