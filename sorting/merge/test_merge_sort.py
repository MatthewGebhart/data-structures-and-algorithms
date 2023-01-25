import pytest
from merge_sort import merge_sort


# @pytest.mark.skip("TODO")
def test_merge_sort_exists():
    assert merge_sort


# @pytest.mark.skip("TODO")
def test_merge_sort_input_list():
    actual = merge_sort([8, 4, 23, 42, 16, 15])
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_merge_sort_empty_list():
    actual = merge_sort([])
    expected = []
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_merge_sort_reverse_sorted():
    actual = merge_sort([28, 16, 11, 9, 5, -1])
    expected = [-1, 5, 9, 11, 16, 28]
    assert actual == expected
