#!/usr/bin/env python

def heapify(array, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and array[child] < array[child + 1]:
            child += 1
        if array[root] < array[child]:
            array[root], array[child] = array[child], array[root]
            root = child
        else:
            break

def heapsort(array):
    for start in range((len(array) - 2) // 2, -1, -1):
        heapify(array, start=start, end=len(array)-1)
    for end in range(len(array) - 1, 0, -1):
        (array[0], array[end]) = (array[end], array[0])
        heapify(array, 0, end - 1)
    return array
