from twttr import shorten

def test():
    assert shorten("twitter") == "twttr"
    assert shorten("name") == "nm"

def test_upper():
    assert shorten("FACEBOOK") == "FCBK"
    assert shorten("WHATSAPP") == "WHTSPP"

def test_num():
    assert shorten("HELLO123") == "HLL123"
    assert shorten("HI456") == "H456"

def test_punc():
    assert shorten("NOOO!!!") == "N!!!"
    assert shorten("HELLO?") == "HLL?"

