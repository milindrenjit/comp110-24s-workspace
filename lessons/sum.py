"""Summing the elements of a list using different loops."""

__author__ = "730531221"


def w_sum(vals: list[float]) -> float:
    """Takes in the list of floats, and returns the sum of all the elements using while loops."""
    sum: float = 0
    index = 0
    while index < len(vals):
        sum += vals[index]
        index += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Takes in the list of floats, and returns the sum of all the elements using for loops."""
    sum: float = 0
    for item in vals:
        sum += item
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Takes in the list of floats, and returns teh sum of all the elements using a range loop."""
    sum: float = 0
    for index in range(len(vals)):
        sum += vals[index]
    return sum