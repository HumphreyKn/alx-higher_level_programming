#!/usr/bin/python3
def uniq_add(my_list=[]):
    # create a new set
    # add the list elements in the set
    new_set = set(my_list)
    total = 0

    for i in new_set:
        total += i

    return total
