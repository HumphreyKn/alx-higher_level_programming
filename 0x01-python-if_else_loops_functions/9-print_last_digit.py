#!/usr/bin/python3
def print_last_digit(num):
    last = abs(num) % 10
    print(last, end="")
    return last
