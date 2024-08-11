# REVERSE OF A NUMBER

# Using Lists
num = input("Enter number:")
rev = num[::-1]
print(rev)

# Using Loops
number = int(input("Enter number:"))
c = 0
while number != 0:
    a = number % 10
    c = c*10 + a
    number //= 10
print(c)
