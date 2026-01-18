def main():
    exp = input("Expression: ")
    var1,xp,var2 = exp.split(" ")
    var1 = float(var1)
    var2 = float(var2)
    match xp:
        case '+':
            print(var1+var2)
        case '-':
            print(var1-var2)
        case '*':
            print(f"{var1*var2:.1f}")
        case '/':
            print(f"{var1/var2:.1f}")
    return 0


main()