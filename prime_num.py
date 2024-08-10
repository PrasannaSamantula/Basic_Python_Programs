# PRIME NUMBER CHECKER
def prime(num):
    isprime = True
    if num == 1:
        isprime = False
    for i in range(2, num):
        if num % i == 0:
            isprime = True
        else:
            isprime = False
    if isprime:
        print("PRIME")
    else:
        print("NOT PRIME")


n = int(input("Enter number:"))
prime(n)
