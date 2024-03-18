#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    newstr = my_list[:]
    if idx < 0:
        return (newstr)
    if idx > len(my-list) - 1:
        return (newstr)
    newstr[idx] = element
    return (newstr]
