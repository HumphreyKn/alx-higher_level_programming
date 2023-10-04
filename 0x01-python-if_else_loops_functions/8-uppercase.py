#!/usr/bin/python3
def uppercase(x):
    for i in x:
        if ord(i) >= 97 and ord(i) <= 122:
            ch = chr(ord(i) - 32)
        else:
            ch = i
        print("{}".format(ch), end="")
    print()
