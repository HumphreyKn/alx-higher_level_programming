#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == "+":
        print("{0} + {1} = {2}".format(a, b, int(add(a, b))))
    elif argv[2] == "-":
        print("{0} - {1} = {2}".format(a, b, int(sub(a, b))))
    elif argv[2] == "*":
        print("{0} * {1} = {2}".format(a, b, int(mul(a, b))))
    elif argv[2] == "/":
        print("{0} / {1} = {2}".format(a, b, int(div(a, b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
