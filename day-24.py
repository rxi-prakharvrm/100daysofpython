tup = (1) # it's an integer <class 'int'>
tup = (1, ) # it's a tuple <class 'tuple'>

tup = (1, 2, 3, 4, "hello", True, 2, 2)
# print(type(tup), tup)
# print(tup[0])
# print(tup[2])
print(tup.index(2, 5, len(tup)))
# print(tup[100]) # tuple index out of range
