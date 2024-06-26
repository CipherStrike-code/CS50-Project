from working import convert
import pytest

def main():
    test_convert()
    test_dash()
    test_hours()
    test_minutes()

def test_convert():
    assert convert("9 AM to 5 PM") == '09:00 to 17:00'
    assert convert("9:00 AM to 5:00 PM") == '09:00 to 17:00'
    assert convert("10 PM to 8 AM") == '22:00 to 08:00'
    assert convert("10:30 PM to 8:50 AM") == '22:30 to 08:50'

def test_dash():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")

def test_unknown_to():
    with pytest.raises(ValueError):
        convert("10:30 PM - 8:50 AM")
    with pytest.raises(ValueError):
        convert("10:30 PM 8:50 AM")

def test_hours():
    with pytest.raises(ValueError):
        convert("13:00 AM to 8:50 PM")
    with pytest.raises(ValueError):
        convert("13 AM to 13 PM")

def test_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")

if __name__ == "__main__":
    main()
