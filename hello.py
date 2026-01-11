#print("What's your name")
name = input("what's your name? ")
print("hello, world"+name)

def calculator():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    return a+b;

def fcalculator():
    a = float(input("Enter a: "))
    b = float(input ("Enter b: "))
    c = a+b;
    print(f"{c:.2f}")

def fprint():
    name = input("Enter your name: ")
    print(f"Hi {name}")

def endprint():
    name = input("Enter your name: ")
    print("hi",end=" ")
    print(name)

print(calculator())
fcalculator()
fprint()
endprint()
