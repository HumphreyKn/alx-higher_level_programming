#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) > 2:
        total = int(argv[1])
        for i in argv[2:]:
            total += int(i)
        print(total)
    elif len(argv) == 2:
        total = int(argv[1])
        print(total)
    else:
        print(0)
