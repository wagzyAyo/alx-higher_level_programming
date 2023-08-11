#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    total = 0
    for add in range( len(sys.argv) - 1):
        total += int(sys.argv[add + 1])
        print("{}".format(total))
