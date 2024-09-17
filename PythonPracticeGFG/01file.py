# Python program to interchange first and last elements in a list

numbers = [1, 2, 3, 4, 5]
# numbers = numbers[-1:] + numbers[1:-1] + numbers[:1]
# numbers[-1], numbers[0] = numbers[0], numbers[-1]
first, *middle, last = numbers
numbers = [last, *middle, first]
print(numbers)