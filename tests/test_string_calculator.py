from src.string_calculator import add

def test_newline_as_delimiter():
    assert add("1\n2,3") == 6