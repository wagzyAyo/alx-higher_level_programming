#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    element = 0
    for i in range(x):
        try:
            if type(my_list[i]) == int:
                print("{:d}".format(mylist[i]), end="")
                element += 1
        except IndexError:
            break
    print()
    return element
