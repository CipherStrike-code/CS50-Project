import re

def main():
    print(validate(input("IPv4 Address: ").strip()))

def validate(ip):
    matches = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$",ip)
    if matches:
        if int(matches.group(1)) <= 255 and int(matches.group(2)) <= 255 and int(matches.group(3)) <= 255 and int(matches.group(4)) <= 255:
            return True
        else:
            return False
    else:
        return False
    
if __name__ == "__main__":
    main()
