"""Mutating functions."""

__author__ = "730531221"

def manual_append(ListA: list[int], add: int) -> None:
    """Append a variable into the list."""
    ListA.append(add)
    return None

def double(ListA: list[int]) -> None:
    """Doubles all items in the list."""
    item = 0
    while item < len(ListA):
        ListA[item] *= 2
        item += 1
    return None
