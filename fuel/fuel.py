def main():
    print(fuel("Fraction: "))

def fuel(prompt):
    while True:
        try:
            #fuel = round(int(input(prompt)*100))
            fuel = input(prompt)
            x,y = fuel.split("/")
            x = int(x)
            y = int(y)
            calc = round((x/y)*100)
            if x>y or y=="0":
                continue
            elif calc<=1:
                return "E"
            elif calc>=99:
                return "F"
            else:
                return f"{calc}%"

        except (ValueError, ZeroDivisionError):
            pass

main()