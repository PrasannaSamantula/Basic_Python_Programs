s1 = {12, 12, "hello", 89.45, True, 1}
s2 = set()
print(s1)
print(type(s1))
print(type(s2))

s1.add("hi")
print(s1)
s1.add((12, 45, 67))    # we can add tuples but not lists since they are mutable
print(s1)
print(len(s1))

s1.remove("hello")  # not present,error
print(s1)

s1.discard("hi")    # not present,no error
print(s1)

s1.pop()    # removes random item
print(s1)
print("----------------------------------")

s3 = {1, 2, 3, 4, 5}
s4 = {4, 5, 6, 10, 11}
s5 = {"janu", "prassu", 90}
""" print(s3.union(s4))
print(s4.union(s3, s5))
print(s3 | s4 | s5)

s3.update([89, "hello"])
print(s3)
s3  |= s5
print(s3)

print(s3.intersection(s4))
print(s3.intersection([4, 2, 6]))
print(s3 & s4)

s3.intersection_update(s4)      # updates set3 with intsersection of s3 & s4
print(s3) 

print(s3.difference(s4))
print(s4.difference([4, 5, 11]))
s4 -= s3
print(s4)   

s3.difference_update(s4)
print(s3)

print(s3.symmetric_difference(s4))
print(s3 ^ s4 ^ s5)
s5.symmetric_difference_update(s3)
print(s3)
print(s5)                   """

print(s3.isdisjoint(s5))
print(s4.isdisjoint(["ram", 6]))

s6 = {1, 2, 3, 4, 5}
print(s3.issubset(s6))      # every element of s3 should be in s6
print(s3.issubset(["hi"]))
print(s3 <= s6)         # subset

print(s3.issubset(s6))      # every element of s6 should be in s3
print(s3 >= s6)

s3.clear()
print(s3)

del s4
print(s4)
