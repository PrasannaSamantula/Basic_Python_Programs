# ARMSTRONG

num = int(input("Enter number:"))
sum = 0
temp = num
while temp > 0:
    rem = temp % 10
    sum += rem ** 3
    temp //= 10
if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")