from src.string_calculator import add

def test_custom_delimiter():
    assert add("//;\n1;2") == 3