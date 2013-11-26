#!/usr/bin/env python

def split(array):
    half = len(array) // 2
    pivot = array[half]
    del(array[half])
    array1 = []
    array2 = []
    for element in array:
        if element < pivot:
            array1.append(element)
        else:
            array2.append(element)
    return (array1, pivot, array2)

def merge(array1, pivot, array2):
    return array1 + [pivot] + array2

def quicksort(array):
    if len(array) <= 1:
        return array
    (array1, pivot, array2) = split(array)
    return merge(quicksort(array1), pivot, quicksort(array2))
