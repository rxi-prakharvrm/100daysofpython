list = [1, 2, 3, 4, 5, "Hello", 6, 7, 8, "World"]

print(list[0:len(list):1])
print(list[:len(list):1])
print(list[0::1])
print(list[::])

print(list[::2])
print(list[5::4])

# List Comprehension

list = [i for i in range(1, 11, 2)]
print(list)

# print all the even numbers upto 100 using list comprehension
print([i for i in range(2, 101, 2)])

#print the squares of all the numbers from 1 to 30 using list comprehension
print([i * i for i in range(1, 31)])

#print the squares of all the numbers from 1 to 30 excluding the those numbers whose square is a prime number
def isPrime(num):
    count = 0
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if(num % i == 0):
            return False
    return True
    
print([i * i for i in range(1, 31) if not isPrime(i)])
