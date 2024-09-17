# arrays in python

# arr1 = [1, 2, 3]
# arr2 = [[1, 2, 3], [4, 5, 6]]
# arr3 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]

# print(arr1)
# print(arr1[0])

# print(arr2)
# print(arr2[0])
# print(arr2[0][0])

# print(arr3)
# print(arr3[0])
# print(arr3[0][0])
# print(arr3[0][0][0])

# arrays using list comprehension in python
m = 10
arr = [0 for i in range(m)]

m = 10
n = 20
arr = [[0 for i in range(m)] for i in range(n)]

m = 3
n = 2
q = 5

# Create a 3D array with dimensions [q][n][m]
arr = [[[0 for _ in range(q)] for _ in range(n)] for _ in range(m)]

# Iterate using q, n, m to match the array's structure
for i in range(m):
    for j in range(n):
        for k in range(q):
            print(arr[i][j][k], end=" ")
        print()
    print()
