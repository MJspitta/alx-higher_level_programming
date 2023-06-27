#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    no_elements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            no_elements += 1
        except (TypeError, ValueError):
            pass
    print()
    return no_elements
