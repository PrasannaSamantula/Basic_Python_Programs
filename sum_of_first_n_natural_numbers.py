# SUM OF FIRST N NATURAL NUMBERS

# Using While Loop
n = int(input("Enter number upto which you want sum:"))
i = 1
count = 0
while i <= n:
    count += i
    i +=1
print(count)

# Using for loop
num = int(input("Enter number upto which you want sum:"))
sum_f = 0
for i in range(1,num+1):
    sum_f += i
print(sum_f)

# Using Functions
def add(number):
    sum_fn=0
    for j in range(1, number + 1):
        sum_fn += j
    return sum_fn
n = int(input("Enter number upto which you want sum:"))
res = add(n)
print(res)
