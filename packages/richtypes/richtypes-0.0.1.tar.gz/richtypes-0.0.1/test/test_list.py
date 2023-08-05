from richtypes import RichList
import pytest


def is_even(num):
    return num % 2 == 0


def test_length(rich_list, rich_list_empty):
    """
    Asserts that the length of rich_list is 11 and the length of rich_list_empty is 0.

    :param rich_list: A list of elements.
    :type rich_list: list
    :param rich_list_empty: An empty list.
    :type rich_list_empty: list
    :return: None
    :rtype: None
    """
    assert rich_list.length == 11
    assert rich_list_empty.length == 0


def test_is_empty(rich_list, rich_list_empty):
    assert rich_list.is_empty == False
    assert rich_list_empty.is_empty == True


def test_is_not_empty(rich_list, rich_list_empty):
    assert rich_list.is_not_empty == True
    assert rich_list_empty.is_not_empty == False


def test_first(rich_list, rich_list_empty):
    assert rich_list.first == 1
    with pytest.raises(Exception):
        assert rich_list_empty.first


def test_first_or_none(rich_list, rich_list_empty):
    assert rich_list.first_or_none == 1
    assert rich_list_empty.first_or_none == None


def test_last(rich_list, rich_list_empty):
    assert rich_list.last == 11
    with pytest.raises(Exception):
        assert rich_list_empty.last


def test_last_or_none(rich_list, rich_list_empty):
    assert rich_list.last_or_none == 11
    assert rich_list_empty.last_or_none == None


def test_where(rich_list):
    assert rich_list.where(is_even, inplace=False) == RichList(2, 4, 6, 8, 10)
    rich_list.where(is_even)
    assert rich_list == RichList(2, 4, 6, 8, 10)


def test_where_not(rich_list):
    assert rich_list.where_not(is_even, inplace=False) == RichList(1, 3, 5, 7, 9, 11)
    assert rich_list != RichList(1, 3, 5, 7, 9, 11)
    rich_list.where_not(is_even)
    assert rich_list == RichList(1, 3, 5, 7, 9, 11)


def test_first_where(rich_list):
    assert rich_list.first_where(is_even) == 2


def test_last_where(rich_list):
    assert rich_list.last_where(is_even) == 10
