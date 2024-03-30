from fuel import convert, gauge
import pytest

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    with pytest.raises(ValueError):
        assert convert("cat/cat")
    with pytest.raises(ZeroDivisionError):
        assert convert("9/0")

def test_fuel():
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"