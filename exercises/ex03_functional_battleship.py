"""EX03 - Functional Battleship."""

__author__ = "730531221"

def input_guess(grid: int, row_or_column: str) -> int:
    """Given int of grid and string row/column, outputs the int for user guess."""
    assert row_or_column == "row" or row_or_column == "column"
    Player_1_guess = int(input(f"Guess a {row_or_column}: "))
    while (Player_1_guess > grid or Player_1_guess < 1):
        Player_1_guess = int(input(f"The grid is only {grid} by {grid}. Try again: "))
    return Player_1_guess

def print_grid(grid: int, row: int, column: int, correct: bool) -> None:
    """Given int grid, int row, int column, and bool is true, prints grid."""
    row_count = 1
    column_count =1 
    while (row_count <= grid):
        if (row_count != row):
            print("\U0001F7E6" * grid)
            row += 1
        elif (row_count == row):
            add_item = ""
            correct_row = ""
            while (column_count <= grid):
                if(column_count == column):
                    if correct is True:
                        add_item  = "\U0001F7E5"
                    else:
                        add_item = "\U00002B1C"
                else:
                    add_item = "\U0001F7E6"
                correct_row = correct_row + add_item
                column_count += 1
            print(correct_row)
            row_count += 1

def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    """Given int secret row, int secret column, int guess row, and int guess column, puts out a bool."""
    if secret_row == guess_row and secret_column == guess_column:
        return True
    else:
        return False
    
def main(grid: int, secret_row: int, secret_column: int) -> None:
    """Given int grid, int secret row, int secret column, will run battleship."""
    turn = 1
    while (turn <= 5):
        print(f"=== Turn {turn}/5 ===")
        row = input_guess(grid, "row")
        column = input_guess (grid, "column")
        print_grid(grid, row, column, correct_guess(secret_row, secret_column, row, column))
        if correct_guess(secret_row, secret_column, row, column) is True:
            print("Hit!")
            print(f"You won in {turn}/5 turns!")
            turn += 6
        else:
            print("Miss!")
            turn += 1
    print("X/5 - Better luck next time!")

if __name__ == "__main__":
    grid: int = random.randint(3,5)
    main(grid, random.randint(1, grid), random.randint(1, grid))
    