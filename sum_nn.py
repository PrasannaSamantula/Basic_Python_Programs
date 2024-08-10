# SUM OF N NATURAL NUMBERS

# Using While loop
n = int(input("Enter no.of elements:"))
i = 0
sum_n = 0
while i < n:
    num = int(input("Enter number:"))
    sum_n += num
    i += 1
print(sum_n)


# Using For Loop
n = int(input("Enter no.of elements:"))
sum_n = 0
for i in range(0,n):
    num = int(input("Enter number:"))
    sum_n += num
print(sum_n)


# Using Functions
def sum_nn(n):
    sum_n = 0
    for i in range(0, n):
        a = int(input("Enter number:"))
        sum_n += a
    print(sum_n)
num = int(input("Enter no.of elements:"))
sum_nn(num)
