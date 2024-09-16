# i = 10
# while i > 0:
#     print(i, end=" ")
#     i -= 1
# else:
#     print()
#     print("Numbers has been printed!")


# Emulate do while loop

# i = 10
# def content():
#     global i
#     print(i, end=" ")
#     i -= 1

# content()
# while i > 0:
#     content()
# else:
#     print()
#     print("Numbers has been printed!")

i = 0
while True:
    print(i, end=" ")
    i += 1
    if(i % 100 == 0):
        break 