import pytest
from src.string_calculator import add

def test_negative_numbers():
    with pytest.raises(ValueError) as e:
        add("1,-2,-3")
    assert str(e.value) == "Negatives not allowed: -2,-3"
