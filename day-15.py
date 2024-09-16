'''
Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
'''
# practice

'''
import time

print(time.gmtime(0))
print(time.time())
print(time.ctime())

# for i in range(0, 4):
#     time.sleep(1)
#     print(i + 1, end=" ")

print(time.localtime())
'''

'''
import time

# Get current hour, minute, and second
current_time = time.localtime()
hour = current_time.tm_hour
minute = current_time.tm_min
second = current_time.tm_sec

# Check the current time and print the appropriate greeting
if 0 <= hour < 12:
    print("Good Morning!")
elif 12 <= hour < 18:
    print("Good Afternoon!")
elif 18 <= hour < 21:
    print("Good Evening!")
else:
    print("Good Night!")
'''

import time

# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)

if 0 <= int(time.strftime('%H')) < 12:
    print("Good Morning!")
elif 12 <= int(time.strftime('%H')) < 18:
    print("Good Afternoon!")
elif 18 <= int(time.strftime('%H')) < 21:
    print("Good Evening!")
else:
    print("Good Night!")