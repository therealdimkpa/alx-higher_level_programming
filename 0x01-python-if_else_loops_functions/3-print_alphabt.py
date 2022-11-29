#!/usr/bin/python3
for item in range (ord('a'), ord('z') + 1):
    if item != ord('e') or item != ord('z'):
        print("{:c}".format(item), end="")
