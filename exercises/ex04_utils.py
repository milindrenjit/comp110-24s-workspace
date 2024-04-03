"""EX04 - List Utility Functions."""


__author__ = "730531221"


def all(int_list: list[int], num: int) -> bool: 
    """Funtion runs through the numbers in int list and checks to see if all of the numbers in the list equals num."""
    if len(int_list) == 0:
        return False
    for i in range(len(int_list)):
        if int_list[i] != num:
            return False
    return True


def max(int_list: list[int]) -> int:
    """Funtion chooses the max number out of the list."""
    if len(int_list) == 0:
        raise ValueError("max() arg is an empty List")
    top_int: int = int_list[0]
    for i in range(len(int_list)):
        if int_list[i] > top_int:
            top_int = int_list[i] 
    return top_int


def is_equal(int_list: list[int], int_list_2: list[int]) -> bool:
    """Function checks if the lists are the same.""" 
    if len(int_list) != len(int_list_2):
        return False
    for i in range(len(int_list)):
        if int_list[i] != int_list_2[i]:
            return False
    return True
        

def extend(int_list: list[int], int_list_2: list[int]) -> None:
    """Function combines both lists."""
    for i in range(len(int_list_2)):
        int_list. append(int_list_2[i])