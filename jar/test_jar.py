from jar import Jar
import pytest

jar = Jar()

def main():
    test_str()
    test_deposit()
    test_withdraw()

def test_init():
    jar = Jar()

def test_str():
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(10)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    with pytest.raises(ValueError):
        jar.deposit(2)

def test_withdraw():
    with pytest.raises(ValueError):
        jar.withdraw(13)

if __name__ == "__main__":
    main()
