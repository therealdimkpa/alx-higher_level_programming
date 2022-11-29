#!/usr/bin/python3
for item in range(0, 100):
    if item != 99:
        print(f"{item:02}", end=", ")
    else:
        print(f"{item}")
