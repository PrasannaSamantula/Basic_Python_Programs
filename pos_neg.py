# POSITIVE OR NEGATIVE NUMBER

# DECISION-MAKING
num = int(input("Enter a number:"))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


#  FUNCTIONS
def pos(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"
n = int(input("Enter a number:"))
res = pos(n)
print(res)