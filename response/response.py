import validators

def main():
    print(validate(input("Enter your email address: ")))

def validate(email):
    if validators.email(email) == True:
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
