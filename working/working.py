import re

def main():
    print(convert(input("Hours: ")))


def convert(s):
    valid = re.search(r"^(\d[0-2]?):?([0-5]\d)? ([A-P]M) (to) (\d[0-2]?):?([0-5]\d)? ([A-P]M)$",s)
    if valid:
        if int(valid.group(1)) > 12 or int(valid.group(5)) > 12:
            raise ValueError
        else:
            if valid.group(4) == None:
                raise ValueError
            else:
                first_time = time(valid.group(1),valid.group(2),valid.group(3))
                last_time = time(valid.group(5),valid.group(6),valid.group(7))
                return first_time + ' to ' + last_time
    else:
        raise ValueError



def time(hr,min,time):
    if time == "AM":
        if hr == "12":
            if min == None:
                new_time = (f"{0:02}"+ ":" + "00")
            else:
                new_time = (f"{0:02}"+ ":" + min)
        else:
            if min == None:
                new_time = (f"{int(hr):02}"+ ":" + "00")
            else:
                new_time = (f"{int(hr):02}"+ ":" + min)
    elif time == "PM":
        if int(hr) == 12:
            if min == None:
                new_time = (f"{int(hr):02}"+ ":" + "00")
            else:
                new_time = (f"{int(hr):02}"+ ":" + min)
        else:
            if min == None:
                new_time = (f"{int(hr)+12:02}"+ ":" + "00")
            else:
                new_time = (f"{int(hr)+12:02}"+ ":" + min)
    return new_time

if __name__ == "__main__":
    main()
