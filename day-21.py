def sum(a, b):
    print(a + b)

sum(10, 20)

def sum(a = 10, b = 20):
    print(a + b)

sum(100, 200)

# Default argument must follow non-default argument
# def sum(a = 10, b):
#     pass

def sum(a, b = 20):
    print(a + b)

sum(10)

def sum(a, b, c = 1):
    print(a + b + c)

sum(2, 3)

# function and variable name can be same in the same function definition
def sum(*numbers): # takes numbers as tuple
    sum = 0
    for ele in numbers:
        sum += ele
    print(sum)

sum(1, 2, 3, 4, 5)

def average(*numbers): # takes numbers as tuple
    sum = 0
    for ele in numbers:
        sum += ele
    print("Average: ", sum / len(numbers))

average(1, 2, 3, 4, 5)

# passing arguments as dictionary
def printFullName(**name):
    print(name["fname"], name["lname"])

printFullName(fname = "Prakhar", lname = "Verma")
