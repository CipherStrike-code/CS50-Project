def main():
    grocery = {}
    while True:
        try:
            items=input("").lower()
            if items != "":
                if items not in grocery:
                    grocery[items] = 1
                else:
                    grocery[items] += 1
            else:
                main()

        except EOFError:
            print("")
            sorted_dict = dict(sorted(grocery.items()))
            for items in sorted_dict:
                print(sorted_dict[items], items.upper(),sep=" ")
            break

main()



