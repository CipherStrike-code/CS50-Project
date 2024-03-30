import sys

def file_checker(file):
    if file.lstrip().startswith("#"):
        return False
    if file.isspace():
        return False
    return True

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) == 2:
        if (sys.argv[1]).endswith(".py"):
            try:
                with open(sys.argv[1], "r") as file:
                    lines = file.readlines()
                count = 0
                for line in lines:
                    if file_checker(line) == True:
                        count += 1
                print(count)
            except FileNotFoundError:
                sys.exit("File does not exist")
        else:
            sys.exit("Not a python file")

    else:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__":
    main()
