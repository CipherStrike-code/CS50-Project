def main():
    plate = input("Plate: ")
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if s[0:2].isalpha() and 6>=len(s)>=2 and s.isalnum():
        #return True
        for i in s:
            if i.isdigit():
                num = s[s.index(i):]
                if num[0]!="0" and num[0:].isdigit():
                    return True
                else:
                    return False
            elif s.isalpha():
                return True
    else:
        return False

if __name__ == "__main__":
    main()