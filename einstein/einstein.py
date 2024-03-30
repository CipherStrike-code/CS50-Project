#main
def main():
    #call for input of user
    mass = int(input("m: "))

    #call for calc function
    j = calc(mass)

    #print out the Number of joules
    print(f"E: {j}")

#calc
def calc(m):
    c = 300000000
    energy = m * pow(c,2)
    return energy

main()