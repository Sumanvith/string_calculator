import pytest
from src.string_calculator import add

def test_ignore_large_numbers():
    assert add("2,1001") == 2

