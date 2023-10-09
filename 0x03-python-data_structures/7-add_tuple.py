#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements
    tup_a = tuple_a + (0, 0)
    tup_b = tuple_b + (0, 0)

    sum_1 = 0
    sum_2 = 0

    sum_1 += int(tup_a[0]) + int(tup_b[0])
    sum_2 += int(tup_a[1]) + int(tup_b[1])

    return (sum_1, sum_2)
