#!/usr/bin/env python

def insertionsort(array):
    for i in range(1, len(array)):
        for j in range(0, i + 1):
            if not array[j] < array[i]:
                break
        tmp = array[i]
        for k in range(i, j, -1):
            array[k] = array[k - 1]
        array[j] = tmp
    return array
