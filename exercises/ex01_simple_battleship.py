"""EX01 - Simple Battleship."""

__author__ = "730531221"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"
result: str = ""

player_1: int = int(input("Pick a secret boat location between 1 and 4:"))

if player_1 < 1:
    print(f"error {player_1} too low!")
    exit()
if player_1 > 4:
    print(f"error {player_1} too high!")
    exit()

player_2: int = int(input("Guess a number between 1 and 4:"))
if player_2 < 1:
    print(f"error {player_2} too low!")
    exit()
if player_2 > 5:
    print(f"error {player_2} too high!")
    exit()
if player_1 == player_2:
    result = RED_BOX
    print("Correct! You hit the ship.")
else:
    result = WHITE_BOX
    print("Incorrect! You missed the ship.")

if player_2 == 1:
    print(result + BLUE_BOX + BLUE_BOX + BLUE_BOX)
if player_2 == 2:
    print(BLUE_BOX + result + BLUE_BOX + BLUE_BOX)
if player_2 == 3:
    print(BLUE_BOX + BLUE_BOX + result + BLUE_BOX)
if player_2 == 4:
    print(BLUE_BOX + BLUE_BOX + BLUE_BOX + result)
