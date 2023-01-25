import pytest
from insertion_sort import insertion_sort


# @pytest.mark.skip("TODO")
def test_insertion_sort_exists():
    assert insertion_sort


# @pytest.mark.skip("TODO")
def test_input_list():
    actual = insertion_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_reverse():
    actual = insertion_sort([20, 18, 12, 8, 5, -2])
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_empty_list():
    actual = insertion_sort([])
    expected = []
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_multiples():
    actual = insertion_sort([5, 12, 7, 5, 5, 7])
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

