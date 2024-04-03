"""Splitting a dictionary into two lists."""


__author__ = "730531221"


def get_keys(dict_1: dict[str, int]) -> list[str]:
    """Takes in a dictionary and returns a list with only keys."""
    returned_list_1: list[str] = list()
    for key in dict_1:
        returned_list_1.append(key)
    return returned_list_1


def get_values(dict_2: dict[str, int]) -> list[int]:
    """Takes in a dictionary and returns a list with only keys."""
    returned_list_2: list[int] = list()
    for key in dict_2:
        returned_list_2.append(dict_2[key])
    return returned_list_2