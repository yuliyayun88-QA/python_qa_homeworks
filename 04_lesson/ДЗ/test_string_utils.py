import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("PYTHON", "Python")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("Skypro", "Skypro"),
    ("    ", ""),
    ("   Python", "Python")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", True),
    ("Hello world", "l", True),
    ("Python", "n", True),
    ("12ab25cd", "2", True)
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("S-k-y-p-r-o", "-", "Skypro"),
    ("Hello world", "l", "Heo word"),
    ("test", "t", "es"),
    ("12ab25cd", "2", "1ab5cd")
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   ")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("Skypro  ", "Skypro  "),
    ("Hello,   world", "Hello,   world"),
    (" /nPython", "/nPython")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "s", False),
    ("", "n", False),
    ("12ab25cd", "9", False)
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "s", "Skypro"),
    ("", "l", ""),
    ("test", "test", ""),
    (" 123 ", " ", "123")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
