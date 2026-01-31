import pytest
from validator import validate_text

def test_empty_text():
    with pytest.raises(ValueError):
        validate_text("")

def test_special_characters():
    result = validate_text("Hello@@@!!!###")
    assert result == "Hello!!!"
