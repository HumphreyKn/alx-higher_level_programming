#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
    elif len(argv) == 2:
        print("1 argument:")
    else:
        print("0 arguments.")

    for i, arg in enumerate(argv[1:], start=1):
        print("{0}: {1}".format(i, arg))
