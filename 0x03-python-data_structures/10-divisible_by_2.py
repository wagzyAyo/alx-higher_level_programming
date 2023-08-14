#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    for x in range(my_list):
        if my_list[x] % 2 == 0:
            return True
        else:
            return False
