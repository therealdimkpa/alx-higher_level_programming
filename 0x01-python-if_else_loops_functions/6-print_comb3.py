#!/usr/bin/python3
for num1 in range(0, 8):
    for num2 in range(1, 10):
        if num1 > num2 or num1 == num2:
            continue
        else:
            print("{}{}".format(num1, num2), end=", ")
print("89")
