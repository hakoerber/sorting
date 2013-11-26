#!/usr/bin/env python

def selectionsort(array):
    for i in range(0, len(array)):
        minindex = i
        for j in range(i, len(array)):
            if array[j] < array[minindex]:
                minindex = j
        (array[i], array[minindex]) = (array[minindex], array[i])
    return array
