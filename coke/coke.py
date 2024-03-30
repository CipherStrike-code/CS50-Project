'''
1. Shows amount due
2. Insert coin
3. Shows change owed
4. Only accepts 50,25,10 and 5 cents
Amount Due: 50
Insert Coin: 25
Amount Due: 25
Insert Coin: 25
Change Owed: 0
'''
def main():
    print("Amount due: 50")
    money = int(input("Insert coin: "))
    coke(money)

def coke(money):
    due = 50
    while True:
        if money in [50,25,10,5]:
            due -= money
            if due > 0:
                print(f"Amount Due: {due}")
                money = int(input("Insert coin: "))
            else:
                print(f"Change Owed: {abs(due)}")
                return False
        else:
            print(f"Amount Due: {due}")
            money = int(input("Insert coin: "))









    '''
    amount = 50
    while True:
            if money == 50 or money == 25 or money == 10 or money == 5:
                due = amount - money
                if due>0:
                    print(f"Amount due: {due}")
                    money = int(input("Insert coin: "))
                    due = due - money
                else:
                    change = 0 - due
                    print(f"Change owed: {change}")
                    return False
            else:
                print(f"Amount due: {due}")
                money = int(input("Insert coin: "))
    '''
try:
    main()

except:
     KeyboardInterrupt



















