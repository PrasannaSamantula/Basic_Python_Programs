# GREATEST OF 3 NUMBERS

# Using Conditionals
num1 = int(input("Enter num1:"))
num2 = int(input("Enter num2:"))
num3 = int(input("Enter num3:"))
if num1 > num2 and num1 > num3:
    print(num1,"is greatest")
elif num2 > num1 and num2 > num3:
    print(num2,"is greatest")
else:
    print(num3, "is greatest")

# Using functions
def great(x,y,z):
    if x > y and x > z:
        print(a, "is greatest")
    elif y > x and y > z:
        print(y, "is greatest")
    else:
        print(z, "is greatest")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
great(a,b,c)