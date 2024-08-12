# FIBONACCI SERIES UPTO NTH TERM

# Using While Loop
n = int(input("Enter number upto which you want series:"))
n1 = 0
n2 = 1
count = 0
if n <= 0:
    print("Enter positive integer..")
elif n == 1:
    print(n1)
else:
    while count < n:
        print(n1,end=" ")
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count+=1


# Using For Loop
num = int(input("Enter number upto which you want series:"))
a = 0
b = 1
for i in range(0,num):
    print(a,end=" ")
    c = a + b
    a = b
    b = c