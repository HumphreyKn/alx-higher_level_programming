#!/usr/bin/python3
def print_lat_digit(num):
    last = abs(num) % 10
    print(last, end="")
    return last
