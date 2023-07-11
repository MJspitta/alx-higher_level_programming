#!/usr/bin/python3
""" Pascal's Triangle """


def pascal_triangle(n):
    if n <= 0:
        return []
    pt = [[1]]
    for i in range(1, n):
        rw = [1]
        for j in range(1, i):
            val = pt[i-1][j-1] + pt[i-1][j]
            rw.append(val)
        rw.append(1)
        pt.append(rw)
    return pt
