#!/usr/bin/python3
def weight_average(my_list=[]):
    top = 0
    bottom = 0

    if not my_list:
        return 0
    for x in my_list:
        top += (x[0] * x[1])
        bottom += x[1]
    return top / bottom
