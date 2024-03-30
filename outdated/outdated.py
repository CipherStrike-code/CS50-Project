# 9/8/1636 or September 8, 1636
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            date = date.strip()
            month, day, year = date.split("/")
            if month.isnumeric() and day.isnumeric():
                if int(month) <= 12 and int(day) <= 31:
                    print(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
                    break
            else:
                continue

        else:
            if "," in date:
                date = date.strip()
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                if month in months and int(day) <= 31:
                    print(
                        f"{year}-{str(months.index(month)+1).zfill(2)}-{day.zfill(2)}"
                    )
                    break
                else:
                    continue
    except (EOFError, KeyboardInterrupt):
        break

    except ValueError:
        continue
