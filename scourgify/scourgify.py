import csv
import sys


def main():
    argument_num()
    new_csv = []
    try:
        with open(sys.argv[1]) as file1:
            lines = csv.DictReader(file1)
            for line in lines:
                lastname, firstname = line["name"].split(", ")
                new_csv.append(
                    {
                        'first': firstname,
                        'last': lastname,
                        'house': line["house"],
                    }
                )

        with open(sys.argv[2], 'w') as outfile:
            fieldname = ["first", "last", "house"]
            writer = csv.DictWriter(outfile, fieldnames=fieldname)
            writer.writeheader()
            for row in new_csv:
                writer.writerow(row)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


def argument_num():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(".csv") or sys.argv[2].endswith(".csv"):
            pass
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        sys.exit("Too few command-line arguments")


if __name__ == "__main__":
    main()