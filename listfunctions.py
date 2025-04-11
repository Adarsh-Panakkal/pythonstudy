import numbers

names = [5,4,2,6,8,9,6,4,25,6,4,6,4,58]
names.append(45)
names.insert(1,10)
names.remove(5)
names.pop()
print(names.index(6))
print(5 in names)
print(names)
names.sort()
print(names)
print(names.count(6))
name2 = names.copy()
print(name2)