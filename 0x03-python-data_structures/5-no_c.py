#!/usr/bin/python3
def no_c(str):
    str_list = list(str)
    i = 0
    while i < len(str_list):
        if str_list[i] in ['c', 'C']:
            str_list.pop(i)
        else:
            i += 1
    return "".join(str_list)
