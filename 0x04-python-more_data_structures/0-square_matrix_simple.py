#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # create a new empty matrix
    new_matrix = []

    # pick each row in the matrix
    for row in matrix:
        another_matrix = []
        # iterate over each element in  row
        for element in row:
            # square the element
            another_matrix.append(element ** 2)

        # append each matrix to the new matrix
        new_matrix.append(another_matrix)

    return new_matrix
