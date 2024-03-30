from plates import is_valid

def test_min():
    assert is_valid("HI") == True
    assert is_valid("H") == False

def test_max():
    assert is_valid("Hello") == True
    assert is_valid("Hellothere") == False

def test_num():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_punc():
    assert is_valid("Hello!") == False
    assert is_valid("Hi !") == False

def test_zero():
    assert is_valid("CS05") == False
    assert is_valid("CS50") == True
    
def test_alpha_start():
    assert is_valid("AA") == True
    assert is_valid("A2") == False