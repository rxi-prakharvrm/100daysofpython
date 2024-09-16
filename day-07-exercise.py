'''
Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers. Your program should format the output in a readable manner!
'''

# Solution
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def calculate(a, b):
    print("Sum of a and b is: ", a + b)
    print("Subtraction of a and b is: ", a - b)
    print("Multiplication of a and b is: ", a * b)
    print("Division of a by b is: ", a / b)
    print("Integer Division of a by b is: ", a // b)
    print("Remainder on a divided by b is: ", a % b)

calculate(a, b)