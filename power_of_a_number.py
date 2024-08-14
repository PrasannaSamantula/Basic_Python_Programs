# POWER OF A NUMBER

n = int(input("Enter number:"))
p = int(input("Enter power:"))
print(f"{n}^{p} =",n**p)

# Using Recursion
def calc_power(Num, power_n):
	if power_n == 0:
		return 1
	return Num * calc_power(Num, power_n-1)

num = int(input("Enter number:"))
powe = int(input("Enter power:"))
print(calc_power(num,powe))

# Using Loops
def CalculatePower(Number,Xa):
    Power=1
    for i in range(1, Xa+1):
        Power=Power*Number
    return Power

N = int(input("Enter number:"))
X = int(input("Enter power:"))
print(CalculatePower(N,X))
