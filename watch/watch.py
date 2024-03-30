import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if matches := re.search(r"^<iframe\s.+https?:\/\/(?:www\.)?youtube\.com\/embed\/(\w+).+<\/iframe>$",s):
        url = "https://youtu.be/" + matches.group(1)
        return url

if __name__ == "__main__":
    main()
