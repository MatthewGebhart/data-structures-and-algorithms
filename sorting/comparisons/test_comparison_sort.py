from comparison_sort import sort_by_title, sort_by_year
from movies import movies

# Expected test output of test #1
expected1 = ["The Intouchables", "Valkyrie", "Stardust", "Ratatouille", "City of God", "Memento", "The Shawshank Redemption", "Beetlejuice", "Crocodile Dundee", "The Cotton Club"]

# Expected test output of test #2
expected2 = ["Beetlejuice", "City of God", "The Cotton Club", "Crocodile Dundee", "The Intouchables", "Memento", "Ratatouille", "The Shawshank Redemption", "Stardust", "Valkyrie"];


def test_sort_by_year_exists():
    assert sort_by_year

def test_sort_by_year_empty():
    actual = sort_by_year([])
    expected = []
    assert actual == expected


def test_by_year():
    actual = sort_by_year(movies)
    # print(actual)
    # print(movies)
    global expected1
    assert actual == expected1


def test_sort_by_title_exists():
    assert sort_by_title


def test_sort_by_title_empty():
    actual = sort_by_title([])
    expected = []
    assert actual == expected

def test_by_title():
    actual = sort_by_title(movies)
    global expected2
    assert actual == expected2
