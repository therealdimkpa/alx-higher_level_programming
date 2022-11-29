#!/usr/bin/python3
for item in range(0, 100):
    if item != 99:
        print("{:02}".format(item), end=", ")
    else:
        print("{}".format(item))
