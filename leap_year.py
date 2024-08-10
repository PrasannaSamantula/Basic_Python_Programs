# LEAP YEAR

# Using Conditionals
year = int(input("Enter year:"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a leap year")

# Using Functions
def cal(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("Leap Year")
    else:
        print("Not a leap year")
num = int(input("Enter year:"))
cal(num)