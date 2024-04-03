"""EX02 - One Shot Battleship."""

__author__ = "730531221"

grid_size: int = 4
secret_row: int = 3
secret_column: int = 2
row_wrong: bool = True
column_wrong: bool = True

guess_for_row: int = int(input("Guess a row: "))
if guess_for_row <= grid_size and guess_for_row >= 1:
    row_wrong = False

while row_wrong:
    if guess_for_row <= grid_size and guess_for_row >= 1:
        row_wrong = False
    else:
        guess_for_row = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

guess_for_column: int = int(input("Guess a column: "))
if guess_for_column <= grid_size and guess_for_column >= 1:
    column_wrong = False

while column_wrong:
    if guess_for_column <= grid_size and guess_for_column >= 1:
        column_wrong = False
    else:
        guess_for_column = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""
row_count: int = 1

if guess_for_row == secret_row:
    if guess_for_column == secret_column:
        result = RED_BOX
    else:
        result = WHITE_BOX
else:
    result = WHITE_BOX

while row_count <= grid_size:
    displayed_row: str = ""
    column_count: int = 1
    if guess_for_row == row_count:
        while column_count <= grid_size:
            if guess_for_column == column_count:
                displayed_row += result
            else:
                displayed_row += BLUE_BOX
            column_count += 1
    else:
        while column_count <= grid_size:
            displayed_row += BLUE_BOX
            column_count += 1
    print(displayed_row)
    row_count += 1

if guess_for_row == secret_row and guess_for_column == secret_column:
    print("Hit! ")
elif guess_for_row == secret_row:
    print("Close! Correct row, wrong column. ")
elif guess_for_column == secret_column:
    print("Close! Correct column, wrong row. ")
else:
    print("Miss! ")