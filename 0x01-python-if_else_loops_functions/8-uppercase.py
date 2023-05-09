#!/usr/bin/python3
def uppercase(str):
    for c in range(len(str)):
        if ord(str[c]) > 96 and ord(str[c]) < 123:
            num = 32
        else:
            num = 0
        print("{:c}".format(ord(str[c]) - num), end='')
    print()
