#!/usr/bin/env python

def gnomesort(array):
    i = 0
    while i != len(array) - 1:
        if array[i] > array[i + 1]:
            (array[i], array[i + 1]) = (array[i + 1], array[i])
            if i != 0:
                i -= 1
                continue
        i += 1
    return array
