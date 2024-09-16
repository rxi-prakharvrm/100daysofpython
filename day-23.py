# list methods
list = [11, 23, 5, 18, 63, 5, 23, 5, 44]

# list.append(8)
# list.sort()
# list.reverse()
# list.insert(0, 100)

print(list.index(23))
print(list.count(5))

# newList is a reference of list so reverse function will change the original list
# newList = list
# list.reverse()

# we can make a copy of a list in the following way
newList = list.copy()
newList.reverse()
print(newList)
print(list)

# concatenate two lists
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)