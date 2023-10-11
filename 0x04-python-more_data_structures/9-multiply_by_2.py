#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Create a new dictionary to store the multiplied values
    dict_2 = {}

    # Iterate through the key-value pairs in the input dictionary
    for key, value in a_dictionary.items():
        dict_2[key] = value * 2

    return dict_2
