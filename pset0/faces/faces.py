def main():
    str = input("Please enter your string: ")
    convstr = convert(str)
    print(convstr)
    return 0

def convert(str):
    convstr = str.replace(":)","🙂")
    convstr = convstr.replace(":(","🙁")
    return convstr



main()