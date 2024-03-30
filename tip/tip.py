#main function
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

#Function for converting dollars to float
def dollars_to_float(d):
    dollars = d.replace("$","")
    dollars = float(dollars)
    return dollars

#Function for calculating percentage to float
def percent_to_float(p):
    percent = p.replace("%","")
    percent = float(percent)/100
    print(percent)
    return percent

main()