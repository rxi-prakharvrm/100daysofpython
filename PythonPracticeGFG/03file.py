pat = [1, 3, 2, 1, 2, 3, 1, 0, 1, 3]
for p in pat:
    pass
    print("Hello", end=" ")
    if (p == 0):
        current = p
        break
    elif (p % 2 == 0):
        continue
    print(p, end=" ")

print()
print(current)