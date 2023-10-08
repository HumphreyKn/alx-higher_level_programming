#!/usr/bin/python3
def no_c(my_string):
    to_remove = "Cc"
    new_string = ""

    if my_string is None:
        return
    else:
        for char in my_string:
            if char not in to_remove:
                new_string += char

        return new_string
