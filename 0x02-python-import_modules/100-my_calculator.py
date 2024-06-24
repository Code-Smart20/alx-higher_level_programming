#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    num_args = len(argv)
    if num_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
