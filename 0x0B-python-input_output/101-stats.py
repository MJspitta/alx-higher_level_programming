#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """


import sys


def print_stat(size, stat_codes):
    """ print accumulated metrics """
    print("File size:", size)
    for code in sorted(stat_codes):
        print("{}: {}".format(code, stat_codes[code]))

def comp_metrics():
    """ func that reads stdin line by line and computes metrics """
    size = 0
    stat_codes = {}
    counter = 0
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    try:
        for line in sys.stdin:
            if counter == 10:
                print_stat(size, stat_codes)
                counter = 1
            else:
                counter += 1

            line = line.split()
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if stat_codes.get(line[-2], -1) == -1:
                        stat_codes[line[-2]] = 1
                    else:
                        stat_codes[line[-2]] += 1
            except IndexError:
                pass
        print_stat(size, stat_codes)

    except KeyboardInterrupt:
        print_stat(size, stat_codes)
        raise


if __name__ == '__main__':
    comp_metrics()
