#!/usr/bin/python3

def safe_print_integer(value):
    try:
        print("{}".format(value))
        return TRUE
    except Exception:
        return FALSE
