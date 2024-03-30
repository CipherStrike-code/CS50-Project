def main():
    ans = (input("What is the Answer to the Great Question of Life, the Universe, and Everything: ")).lower().strip()
    print(deep(ans))


def deep(x):
    if x == "42" or x == "forty-two" or x == "forty two":
        return "yes"
    else:
        return "no"

main()




