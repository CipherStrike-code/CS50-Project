import random
import sys


def main():
    count = 0
    question = 0
    score = 0
    level = get_level()
    while question != 10:
        try:
            x, y, sum = generate_integer(level)
            while True:
                ans = int(input(f"{x} + {y} = "))
                if ans == sum:
                    question += 1
                    score += 1
                    break
                else:
                    count += 1
                    if count == 3:
                        print(f"{x} + {y} = {sum}")
                        question += 1
                        count = 0
                        break
                    else:
                        print("EEE")
                        continue

        except ValueError:
            continue
    print(f"Score: {score}")
    sys.exit(0)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 4 > level > 0:
                return level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        sum = x + y
        return x, y, sum
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        sum = x + y
        return x, y, sum
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
        sum = x + y
        return x, y, sum


if __name__ == "__main__":
    main()
