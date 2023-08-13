#!/usr/bin/python3
def no_c(my_string):
    new-string = ''
    for x in my_string:
        if x != "c" and x != "C":
            new-string += x
        return new-string
