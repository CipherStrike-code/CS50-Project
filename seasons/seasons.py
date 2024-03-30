import datetime
import inflect
import sys

def main():
    print(seasons(input("Date of Birth: ")))

def conversion(birth_date):
    Year, Month, Day = birth_date.split("-")
    converted_date = datetime.date(int(Year), int(Month), int(Day))
    return converted_date


def word_convert(numbers):
    inflector = inflect.engine()
    words = inflector.number_to_words(numbers, andword = '')
    return words

def seasons(birth_date):
    try:
        datetime.date.fromisoformat(birth_date)
    except (ValueError, TypeError):
        sys.exit("Invalid date")

    converted_date = conversion(birth_date)
    today = datetime.date.today()
    difference = today - converted_date
    minutes = difference.days * 60 *24
    word = word_convert(minutes)

    return f"You are {word.capitalize()} minutes away from your birth date!!!"

if __name__ == "__main__":
    main()
