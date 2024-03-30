def main():
    word = input("Input your word: ")
    print(shorten(word))


def shorten(word):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    new = ""
    for i in word:
        if i not in vowels:
            new += i
    return new


if __name__ == "__main__":
    main()