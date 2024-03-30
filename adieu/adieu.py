import inflect
import sys

p = inflect.engine()

namelist = []

while True:
    try:
        name = input("Name: ").strip()
        namelist.append(name)
    except EOFError:
            break

if len(namelist)==1:
    print(f"Adieu, adieu, to {namelist[0]}")
elif len(namelist)>1:
    #mylist = p.join(("apple", "banana", "carrot"))
    mylist = p.join(namelist)
    print(f"Adieu, adieu, to {mylist}")
else:
    sys.exit(1)