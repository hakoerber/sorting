#!/usr/bin/env python

def split(array):
    half = len(array) // 2
    return (array[:half], array[half:])

def merge(array1, array2):
    result = []
    while True:
        if len(array1) == 0:
            result.extend(array2)
            break
        if len(array2) == 0:
            result.extend(array1)
            break
        if array1[0] < array2[0]:
            result.append(array1[0])
            del array1[0]
        else:
            result.append(array2[0])
            del array2[0]
    return result

def mergesort(array):
    if len(array) <= 1:
        return array
    (array1, array2) = split(array)
    return merge(mergesort(array1), mergesort(array2))
