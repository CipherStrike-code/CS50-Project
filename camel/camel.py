'''
Checks thru all the letters individually.
For every uppercase letter detected split it, and put
in a a list
'''

def main():
    word = input("What is your word: ")
    print(snake_case(word))

def snake_case(word):
    sc = ""
    for i in word:
        if i.islower():
            sc += i

        elif i.isupper():
            i = i.lower()
            sc += "_" + i

        else:
            return("Alphabets only")
    return sc
main()








