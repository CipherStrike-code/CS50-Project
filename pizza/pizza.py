import csv
import sys
from tabulate import tabulate

def main():
    argument_num()
    rows = []
    try:
        with open(sys.argv[1],"r") as file:
            lines = csv.reader(file)
            for line in lines:
                rows.append(line)
        print(tabulate(rows[1:], headers=rows[0], tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found.")


def argument_num():
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
            pass
        else:
            sys.exit("Not a CSV file")
    elif len(sys.argv)>2:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")

if __name__ == "__main__":
    main()