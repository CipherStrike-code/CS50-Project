from seasons import seasons

def main():
    test_correct()


def test_correct():
    assert(seasons("1999-01-01")) == "Thirteen million, two hundred sixty-eight thousand, one hundred sixty minutes"
    #assert(seasons("2023-03-24")) == "Five hundred twenty-seven thousand forty minutes"


if __name__ == "__main__":
    main()




