import random
import sys

def check(num,guess):
    if guess > num:
        print("Too large!")
        return False
    elif guess < num:
        print("Too small!")
        return False
    else:
        print("Just right!")
        return True

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level>0:
                num = random.randint(1,level)
                while True:
                    guess = int(input("Guess: "))
                    if check(num,guess):
                        sys.exit()
            else:
                continue
        except (ValueError,TimeoutError):
            continue

main()