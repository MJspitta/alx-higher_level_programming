#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        print("$")
    else:
        for i in matrix:
            for j in i:
                if j == i[-1]:
                    print("{:d}".format(j), end='')
                else:
                    print("{:d}".format(j), end=' ')
            print()
