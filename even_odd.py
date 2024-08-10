# EVEN OR ODD

# Using Decision-making
a = int(input("Enter number:"))
if a % 2 == 0:
    print("EVEN")
else:
    print("ODD")


# Using Functions
def func(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
r = int(input("Enter a number:"))
res = func(r)
print(res)