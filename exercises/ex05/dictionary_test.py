"""Dictionary Unit Tests."""

__Author__ = "730531221"

from exercises.ex05.dictionary import invert, favorite_color, count, alphabetizer, update_attendance


def test_invert_maps_properly():
    """This function tests the invert function with a dictionary full of animals and matches to their sounds."""
    animal_sounds = {'dog': 'bark', 'cat': 'meow', 'cow': 'moo'}
    assert invert(animal_sounds) == {'bark': 'dog', 'meow': 'cat', 'moo': 'cow'}


def test_invert_empty_encyclopedia():
    """This function tests the invert function with an empty encyclopedia."""
    empty_encyclopedia = {}
    assert invert(empty_encyclopedia) == {}


def test_invert_with_mirror_images():
    """This function tests the invert function with a dictionary of things that are mirrored and will cause duplicate values."""
    mirrored_images = {'left': 'right', 'up': 'right'}
    try:
        invert(mirrored_images)
        assert False, "Mirror images should cause KeyError"
    except KeyError:
        assert True


def test_favorite_color_in_rainbow():
    """This function tests the favorite color function with some people and relates them to their favorite colors."""
    color_choices = {'Lucy': 'violet', 'Megan': 'indigo', 'Ryan': 'violet'}
    assert favorite_color(color_choices) == 'violet'


def test_favorite_color_monochrome():
    """This function tests the favorite color function when people like the same shade."""
    monochrome_colors = {'Sam': 'grey', 'Ella': 'grey'}
    assert favorite_color(monochrome_colors) == 'grey'


def test_favorite_color_in_vacuum():
    """This function tests the favoritecolor function when no choices are made."""
    vacuum_color = {}
    assert favorite_color(vacuum_color) == ''


def test_count_mix():
    """This function tests the count function with a basket of fruits where some are the same."""
    basket_of_fruits = ['apple', 'orange', 'apple', 'banana']
    assert count(basket_of_fruits) == {'apple': 2, 'orange': 1, 'banana': 1}


def test_count_uniques():
    """This function tests the count function with a bunch of unique gems."""
    gems = ['ruby', 'sapphire', 'emerald']
    assert count(gems) == {'ruby': 1, 'sapphire': 1, 'emerald': 1}


def test_count_empty():
    """This function tests the count function with an empty chest."""
    empty_chest = []
    assert count(empty_chest) == {}


def test_alphabetizer_book_index():
    """This function tests the alphabetizer function with a list of words and sorts them like a book index."""
    index = ['apple', 'ant', 'banana', 'book']
    assert alphabetizer(index) == {'a': ['apple', 'ant'], 'b': ['banana', 'book']}


def test_alphabetizer_mixed_case():
    """This fucntion tests the alphabetizer function with a mix of uppercase and lowercase characters."""
    mixed_case_characters = ['Apple', 'antelope', 'Banana', 'book']
    assert alphabetizer(mixed_case_characters) == {'a': ['Apple', 'antelope'], 'b': ['Banana', 'book']}


def test_alphabetizer_empty_vocabulary():
    """This function tests the alphabetizer function with an empty list of vocab."""
    empty_vocab_list = []
    assert alphabetizer(empty_vocab_list) == {}


def test_update_attendance_school_log():
    """This function tests the update attendance function by adding a student to the school attendance log."""
    attendance_log = {'Monday': ['Alice']}
    update_attendance(attendance_log, 'Monday', 'Bob')
    assert attendance_log == {'Monday': ['Alice', 'Bob']}


def test_update_attendance_new_day():
    """This function tests the update attendance function by logging attendance for the next day."""
    next_log = {'Monday': ['Alice']}
    update_attendance(next_log, 'Tuesday', 'Charlie')
    assert next_log == {'Monday': ['Alice'], 'Tuesday': ['Charlie']}


def test_update_attendance_empty_calendar():
    """This function tests the update attendance function with an empty calendar."""
    empty_cal = {}
    update_attendance(empty_cal, 'Wednesday', 'Daisy')
    assert empty_cal == {'Wednesday': ['Daisy']}