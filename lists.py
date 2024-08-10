list1 = [10, "hi", 9.5, True]
print(list1)
print(type(list1))
print(list1[1])
print(list1[1:])
print(list1[::-1])
print(list1[::3])   # step 3
print(10 in list1)
print(10 not in list1)

list2 = [30, 12, 90, 56, 34]
print(sorted(list2))
print(list1+list2)
print(max(list2))
print(min(list2))


list1.append(34)
print(list1)
list1.extend(["hello", 78])
print(list1)
list1.insert(2, "prasanna")
print(list1)
list1.remove("hi")
print(list1)
list1.pop()         # last element is removed
print(list1)
list1.reverse()
print(list1)
list1.copy()
print(list1)

list1[1:3] = ["a", 65, 65]      # allows duplication
print(list1)

cou = list1.count(65)
print(cou)

del list1
list2.clear()
print(list2)
# print(list1)


# nested list
l = [10, 67, "hello", [4, 78, "hi"], "ok", 90]
print(l[3][2])
print(len(l)-1)
print(l[3])
