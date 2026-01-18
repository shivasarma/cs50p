def main():
    greet = input("Greeting: ")
    greet = greet.strip().lower()
    if(greet == "hello"):
        print("$100")
    elif(greet[0] == 'h'):
        print("$20")
    else:
        print("$0")
    return 0


main()
