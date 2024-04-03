"""Dictionary Utilities."""

__author__ = "730531221"


def invert(dict_1: dict[str, str]) -> dict[str, str]:
    """Function inverts keys and values."""
    dict_a: dict[str, str] = dict()
    for key in dict_1:
        if dict_1[key] in dict_a:
            raise KeyError("This Key Already Exists")
        dict_a[dict_1[key]] = key 
    return dict_a
    

def favorite_color(dict_1: dict[str, str]) -> str:
    """Function identifies favorite color."""
    dict_a: dict[str, int] = dict()
    for key in dict_1:
        color: str = dict_1[key]
        if color in dict_a:
            dict_a[color] += 1
        else:
            dict_a[color] = 1

    pop_color: str = str()
    frequent: int = 0
    for key in dict_a:
        if dict_a[key] > frequent:
            frequent = dict_a[key]
            pop_color = key
    return pop_color


def count(list_1: list[str]) -> dict[str, int]:
    """Function counts values in list."""
    dict_a: dict[str, int] = dict()
    for item in list_1:
        if item in dict_a:
            dict_a[item] += 1
        else:
            dict_a[item] = 1
    return dict_a


def alphabetizer(list_1: list[str]) -> dict[str, list[str]]:
    """Function has dictionary with lists."""
    dict_a: dict[str, list[str]] = dict()
    for item in list_1:
        letter_1: str = item[0].lower()
        if letter_1 in dict_a:
            dict_a[letter_1].append(item)
        else:
            dict_a[letter_1] = [item]
    return dict_a


def update_attendance(dict_1: dict[str, list[str]], day: str, student: str) -> None:
    """Function adds student attendance."""
    if day in dict_1:
        if student not in dict_1[day]:
            dict_1[day].append(student)
    else:
        dict_1[day] = [student]