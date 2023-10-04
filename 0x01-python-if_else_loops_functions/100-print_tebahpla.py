#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        ch = i
    else:
        ch = i - 32
    print("{0}".format(chr(ch)), end="")
