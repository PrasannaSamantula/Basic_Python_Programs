# SUM OF N NATURAL NUMBERS WITHIN GIVEN RANGE

# Using For Loop
start = int(input("Enter starting:"))
end = int(input("Enter ending:"))
sum_nr = 0
for i in range(start,end+1):
    sum_nr += i
print(sum_nr)

# Using Functions
def func(s,e):
    sum_nrp = 0
    for j in range(s, e + 1):
        sum_nrp += j
    print(sum_nrp)
star = int(input("Enter starting:"))
endi = int(input("Enter ending:"))
func(star,endi+1)