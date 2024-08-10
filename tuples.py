t = (23.56, 18, True, "prassu")
t1 = (10,)
t2 = (10)
t3 = (30, 15, 15, 15, 43)
print(t)
print(type(t))
print(type(t1))
print(type(t2))

print(t[2])
print(t[1:4])
print(t[::2])
print(t[-3])

print(len(t))
print(min(t3))
print(max(t3))
print(sum(t3))
print(t3.count(15))
print(t3.index(15))         # first occurence

t4 = (t1, t, t3)
print(t4)
print(t4[1][1])

t5 = t1 + t + t3
print(t5)

t6 = t1 * 5
print(t6)

list1 = [34, 56, "hello"]
print(list1)
print(tuple(list1))

del t5
print(t5)
