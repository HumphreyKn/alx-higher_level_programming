#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed_elements = 0

    try:
        for i in range(x):
            # Try to convert the element to an integer and print if successful
            element = my_list[i]
            if isinstance(element, int):
                print("{:d}".format(element), end="")
                printed_elements += 1
    except (IndexError, ValueError, TypeError):
        pass
    finally:
        print()

    return printed_elements
