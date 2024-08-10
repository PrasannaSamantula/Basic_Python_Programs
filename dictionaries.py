d = {
    "Ram": 1234,
    "Eswar": 9820,
    "Mohan": 4627
}

d1 = {}
print(d)
print(type(d1))
print(d["Eswar"])

d2 = dict([("hi", 38992), ("hello", 39280)])
print(d2)
d2["hello"] = 90134
print(d2)

print(d2.get("hi"))

print(d.items())
print(d.keys())
print(d.values())

del d["Ram"]
print(d)

d.pop("Mohan")
print(d)

d2.clear()
print(d2)

d3 = d.copy()
print(d3)

print(len(d1))
