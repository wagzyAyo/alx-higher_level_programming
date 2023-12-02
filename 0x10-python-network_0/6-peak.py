#!/usr/bin/python3
'''Algorith that find the peak
in a list of integers'''

def find_peak(list_of_integers):
    '''funtion returns peak in a list of integers'''
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # The peak must be on the left side, including mid
            high = mid
        else:
            # The peak must be on the right side, excluding mid
            low = mid + 1

    return list_of_integers[low]
