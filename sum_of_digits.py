# SUM OF DIGITS OF A NUMBER

# Using Loops
num = int(input("Enter number:"))
count = 0
while num > 0:
    rem = num % 10
    count += rem
    num //= 10
print(count)

# Using Functions
def func(n):
    c = 0
    while n > 0:
        r = n % 10
        c += r
        n //= 10
    return c
num1 = int(input("Enter number:"))
a = func(num1)
print(a)
