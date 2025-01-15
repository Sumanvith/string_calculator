import pytest
from src.string_calculator import add

def test_multiple_custom_delimiters():
    assert add("//[***][%%]\n1***2%%3") == 6

def test_multiple_custom_delimiters_with_length():
    assert add("//[***][%%%]\n1***2%%%3") == 6

def test_multiple_custom_delimiters_and_large_numbers():
    assert add("//[;;][##]\n2;;1001##3") == 5
