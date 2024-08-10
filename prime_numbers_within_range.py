def prime(start,end):
    for num in range(start,end+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num,end=" ")
s = int(input("Enter start:"))
e = int(input("Enter end:"))
prime(s,e)
