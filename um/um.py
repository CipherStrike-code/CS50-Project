import re

def main():
    print(count(input("Text: ").strip()))

def count(s):
    s = s.split()
    count = 0
    for word in s:
        if re.search(r"^um[,?.!]*$",word,re.IGNORECASE):
            count+=1
    return count

if __name__ == "__main__":
    main()
