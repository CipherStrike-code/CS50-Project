def main():
    ans = input("What is the Answer to the Great Question of Life, the Universe, and Everything: ").lower().strip()
    print(deep(ans))

def deep(x):
    match x:
        case "42" | "forty-two" | "forty two":
            return "yes"
        case _:
            return "no"

main()


