def find_next_empty(puzzle):
    #finds the next row, column on the puzzle that's not filled yet --> rep with -1
    #return none, none, if there is no empty spaces

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None


def is_valid(puzzle, guess, row, col):
    #figure out whether the guess at the row/col of the puzzle is a valid guess
    #return True if it is valid, False otherwise
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    #to get where the 3x3 square starts and iterate over the 3 values in the row/column
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    #if we get here, these checks pass
    return True


def solve_sudoku(puzzle):
    #choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    #if there is nowhere left, then the game is done
    if row is None:
        return True

    #if there is a place to put a number, then make a guess between 1 to 9
    for guess in range(1, 10):
        #check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
            #if this is valid, then place that guess on the puzzle
            puzzle[row][col] = guess
            #recursively call our function
            if solve_sudoku(puzzle):
                return True

        #if not valid or if our guess does not solve the puzzle, then backtrack and try a new number
        puzzle[row][col] = -1

    #if none of the numbers work, then the puzzle is unsolvable.
    return False


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

