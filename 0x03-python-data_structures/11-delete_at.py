#!/usr/bin/python3
new_list = ''
def delete_at(my_list=[], idx=0):
    if idx < 0 and idx > len(my_list):
        return my_list
    else:
     new_list = del my_list[idx]
     return new_list
