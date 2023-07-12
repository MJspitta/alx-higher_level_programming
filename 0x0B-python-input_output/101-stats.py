#!/usr/bin/python3
""" Script that reads stdin line by line and computes metrics """


import sys
from collections import defaultdict


def comp_metrics():
    """ func that reads stdin line by line and computes metrics """
    size = 0
    stat_codes = defaultdict(int)
    counter = 0

    try:
        for line in sys.stdin:
            counter += 1
            parts = line.strip().split()
            if len(parts) >= 7:
                stat_code = parts[-2]
                fsize = parts[-1]
                size += int(fsize)
                stat_codes[stat_code] += 1

            if counter % 10 == 0:
                print("Total file size:", size)
                for code in sorted(stat_codes.keys()):
                    print("{}: {}".format(code, stat_codes[code]))

    except KeyboardInterrupt:
        print("Total file size:", size)
        for code in sorted(stat_codes.keys()):
            print("{}: {}".format(code, stat_codes[code]))


if __name__ == '__main__':
    comp_metrics()
