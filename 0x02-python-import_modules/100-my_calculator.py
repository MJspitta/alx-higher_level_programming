#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        op = ['+', '-', '*', '-']
        if argv[2] not in op:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        else:
            if argv[2] == '+':
                print("{} {} {} = {}".format(a, argv[2], b, add(a, b)))
            elif argv[2] == '-':
                print("{} {} {} = {}".format(a, argv[2], b, sub(a, b)))
            elif argv[2] == '*':
                print("{} {} {} = {}".format(a, argv[2], b, mul(a, b)))
            elif argv[2] == '/':
                print("{} {} {} = {}".format(a, argv[2], b, div(a, b)))
