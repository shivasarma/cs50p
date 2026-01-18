#Demonstrates formatting with commas

x = float(input("what's x? "))
y = float(input("what's y? "))

z = round(x+y)

#give large digits as input and they throw as us number format
print(f"{z:,}")