import pytest
from src.string_calculator import add

def test_empty_string():
    assert add("") == 0

def test_single_number():
    assert add("1") == 1

def test_two_numbers():
    assert add("1,2") == 3

def test_multiple_numbers():
    assert add("1,2,3,4") == 10

def test_newline_as_delimiter():
    assert add("1\n2,3") == 6

def test_custom_delimiter():
    assert add("//;\n1;2") == 3

def test_negative_numbers():
    with pytest.raises(ValueError) as e:
        add("1,-2,-3")
    assert str(e.value) == "Negatives not allowed: -2,-3"

def test_ignore_large_numbers():
    assert add("2,1001") == 2

def test_multiple_custom_delimiters():
    assert add("//[***][%%]\n1***2%%3") == 6

def test_multiple_custom_delimiters_with_length():
    assert add("//[***][%%%]\n1***2%%%3") == 6

def test_multiple_custom_delimiters_and_large_numbers():
    assert add("//[;;][##]\n2;;1001##3") == 5
