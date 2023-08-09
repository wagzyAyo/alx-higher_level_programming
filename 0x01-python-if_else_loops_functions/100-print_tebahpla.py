#!/usr/bin/python3
for letters in range(ord('z'), ord('a') -1, -1):
    if letters % 2 == 0:
        lett = 0
    else:
        lett = 32
    print("{}".format(chr(letters - lett)), end="")
