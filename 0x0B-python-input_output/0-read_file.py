#!/usr/bin/python3
"""Read a text file and print it to stdout"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""

    with open(filename) as f:
        read_data = f.read()

    print(read_data, end="")
