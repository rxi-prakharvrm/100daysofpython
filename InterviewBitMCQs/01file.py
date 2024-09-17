# numbers = (5, 2, 3, 8, 1, 20)
# sorted_numbers = sorted(numbers)
# even = lambda a : a % 2 == 0
# even_numbers = filter(even, sorted_numbers)
# print(even_numbers)
# print(type(even_numbers))

numbers = (4, 7, 19, 2, 89, 45, 2, 22)
# l = [num for num in numbers if num % 2 != 0]
# print(l)
l = (num for num in numbers if num % 2 != 0) # returns a generator
print(l)
l = tuple(num for num in numbers if num % 2 != 0)
print(l)
sorted_numbers = sorted(numbers)
odd_numbers = [x for x in sorted_numbers if x % 2 != 0]
print(odd_numbers)