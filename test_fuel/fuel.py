def main():
    while True:
        fraction = input("Fraction: ")
        try:
            calc = convert(fraction)
            break
        except (ValueError, ZeroDivisionError):
                continue

    print(gauge(calc))


def convert(fraction):
        try:
            #fuel = round(int(input(prompt)*100))
            x,y = fraction.split("/")
            x = int(x)
            y = int(y)
            calc = round((x/y)*100)
            return calc
        except (ValueError, ZeroDivisionError):
            main()


def gauge(calc):
        calc = int(calc)
        if calc<=1:
            return "E"
        elif calc>=99:
            return "F"
        else:
            return f"{calc}%"


if __name__ == "__main__":
    main()