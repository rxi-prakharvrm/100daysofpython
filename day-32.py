# set operations

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8, 9}

# print(s1.union(s2)) # s1, s2 are untouched
# s1.update(s2) # s1 is updated
# print(s1.intersection(s2)) # s1, s2 are untouched
# s1.intersection_update(s2) # s1 is updated
s1.symmetric_difference(s2) # s1, s2 are untouched

print(s1)