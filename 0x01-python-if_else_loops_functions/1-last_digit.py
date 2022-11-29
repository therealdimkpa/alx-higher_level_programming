#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_num = str(number)
str_num = int(str_num[-1])

if str_num > 5:
    print(f"Last digit of {number} is {str_num} and is greater than 5")
elif str_num == 0:
    print(f"Last digit of {number} is {str_num} and is 0")
else:
    print(f"Last digit of {number} is {str_num} and is less than 6 and not 0")
