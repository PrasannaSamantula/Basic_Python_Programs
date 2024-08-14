# FACTORIAL OF A NUMBER

n = int(input("Enter number:"))
prod = 1
for i in range(n,0,-1):
    prod *= i
print(prod)


num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print(" Factorial does not exist for negative numbers")
elif num == 0:
   print("1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print(factorial)

# Using Recursion
def fact(number):
    if number == 1 or number == 0:
        return 1
    else:
        return number * fact(number - 1)

numb = int(input("Enter number:"))
a = fact(numb)
print(a)