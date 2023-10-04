#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        rem_char = str[:n] + str[n + 1:]
    else:
        rem_char = str
    return rem_char
