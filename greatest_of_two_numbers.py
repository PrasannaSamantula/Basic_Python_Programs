# GREATEST OF 2 NUMBERS


x,y=map(int,input("Enter two numbers with space:").split())
print(x if x>y else y)

# Using Conditionals
a,b = map(int,input("Enter two numbers with space:").split())
if a > b:
    print(a,"is greatest")
else:
    print(b,"is greatest")

# Using Functions
def great(d,e):
    if d > e:
        print(d,"is greatest")
    else:
        print(e,"is greatest")
num1,num2 = map(int,input("Enter two numbers with space:").split())
great(num1,num2)
