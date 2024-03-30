def main():
    ans = input("Expression: ").strip()
    print(calc(ans))

def calc(x):
    a,b,c = x.split(" ")
    a = float(a)
    c = float(c)
    if b == "+":
        ans = a+c
        return ans
    elif b == "-":
        ans = a-c
        return ans
    elif b == "*":
        ans = a*c
        return ans
    elif b == "/":
        ans = a/c
        return ans

main()