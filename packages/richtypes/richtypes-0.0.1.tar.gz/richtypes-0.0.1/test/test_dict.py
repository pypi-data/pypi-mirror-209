from richtypes import RichDict
import pytest


def test_length(rich_dict, rich_dict_empty):
    assert rich_dict.length == 11
    assert rich_dict_empty.length == 0


def test_is_empty(rich_dict, rich_dict_empty):
    assert rich_dict.is_empty == False
    assert rich_dict_empty.is_empty == True


def test_is_not_empty(rich_dict, rich_dict_empty):
    assert rich_dict.is_not_empty == True
    assert rich_dict_empty.is_not_empty == False


def test_first_item(rich_dict, rich_dict_empty):
    assert rich_dict.first_item == {"one": 1}
    with pytest.raises(Exception):
        assert rich_dict_empty.first_item


def test_first_key(rich_dict, rich_dict_empty):
    assert rich_dict.first_key == "one"
    with pytest.raises(Exception):
        assert rich_dict_empty.first_key


def test_first_value(rich_dict, rich_dict_empty):
    assert rich_dict.first_value == 1
    with pytest.raises(Exception):
        assert rich_dict_empty.first_value


def test_first_key_or_none(rich_dict, rich_dict_empty):
    assert rich_dict.first_key_or_none == {"one": 1}
    assert rich_dict_empty.first_key_or_none == None


def test_replace_key(rich_dict):
    assert rich_dict.replace_key("one", "final", inplace=False) == RichDict(
        final=1,
        two=2,
        three=3,
        four=4,
        five=5,
        six=6,
        seven=7,
        eight=8,
        nine=9,
        ten=10,
        eleven=11,
    )
    rich_dict != RichDict(
        one=1,
        two=2,
        three=3,
        four=4,
        five=5,
        six=6,
        seven=7,
        eight=8,
        nine=9,
        ten=10,
        eleven=11,
    )
    rich_dict.replace_key("one", "final")
    assert rich_dict == RichDict(
        final=1,
        two=2,
        three=3,
        four=4,
        five=5,
        six=6,
        seven=7,
        eight=8,
        nine=9,
        ten=10,
        eleven=11,
    )
