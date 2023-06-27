#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    no_elements = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            no_elements += 1
        except IndexError:
            break
    print()
    return no_elements
