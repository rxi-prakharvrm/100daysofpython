# Enumerate

marks = [12, 33, 50, 98, 32, 45, 67, 89]

for index, mark in enumerate(marks):
    print(f"Index: {index}, Mark: {mark}")
    if index == 3:
        print("Wow! You got 98 marks!")
        