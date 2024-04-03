"""Test my garden functions."""


__author__ = "730531221"


from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_existing():
    """Function tests adding a new plant to a kind in the dictionary."""
    garden = {'herb': ['mint', 'basil']}
    add_by_kind(garden, 'herb', 'cilantro')
    assert garden == {'herb': ['mint', 'basil', 'cilantro']}


def test_add_by_kind_new():
    """Function tests adding a plant to a new kind in the dictionary."""
    garden = {'herb': ['mint']}
    add_by_kind(garden, 'shrub', 'hydrangea')
    assert garden == {'herb': ['mint'], 'shrub': ['hydrangea']}


def test_add_by_kind_empty():
    """Function tests adding a plant to an empty dictionary."""
    garden = {}
    add_by_kind(garden, 'tree', 'maple')
    assert garden == {'tree': ['maple']}


def test_add_by_date_existing():
    """Function tests adding a plant to an existing month in the dictionary."""
    garden_by_date = {'March': ['cherry blossom', 'peach blossom']}
    add_by_date(garden_by_date, 'March', 'apple blossom')
    assert garden_by_date == {'March': ['cherry blossom', 'peach blosson', 'apple blossom']}


def test_add_by_date_new():
    """Function tests adding a plant to a new month in the dictionary."""
    garden_by_date = {'March': ['cherry blossom']}
    add_by_date(garden_by_date, 'April', 'tulip')
    assert garden_by_date == {'March': ['cherry blossom'], 'April': ['tulip']}


def test_add_by_date_empty():
    """Function tests adding a plant to an empty dictionary."""
    garden_by_date = {}
    add_by_date(garden_by_date, 'April', 'tulip')
    assert garden_by_date == {'April': ['tulip']}


def test_lookup_by_kind_and_date_exists():
    """Function tests finding a plant that exists in both the kind and date dictionaries."""
    plant_by_kind = {'vegetable': ['tomato', 'cucumber']}
    plant_by_date = {'August': ['tomato', 'corn']}
    result = lookup_by_kind_and_date(plant_by_kind, plant_by_date, 'vegetable', 'August')
    assert result == 'vegetable to plant in August: [\'tomato\']'


def test_lookup_by_kind_and_date_none():
    """Function tests looking up a kind where no plants of that same kind are planted in a specific month."""
    plant_by_kind = {'herb': ['basil', 'thyme']}
    plant_by_date = {'September': ['pumpkin', 'squash']}
    result = lookup_by_kind_and_date(plant_by_kind, plant_by_date, 'herb', 'September')
    assert result == 'herb to plant in September'


def test_lookup_by_kind_and_date_multiple():
    """Functions tests finding multiple plants that exist in both the kind and date dictionaries."""
    plant_by_kind = {'fruit': ['apple', 'pear', 'peach']}
    plant_by_date = {'October': ['pear', 'apple', 'grape']}
    result = lookup_by_kind_and_date(plant_by_kind, plant_by_date, 'fruit', 'October')
    assert result == 'fruits to plant in October: [\'apple\', \'pear\']'