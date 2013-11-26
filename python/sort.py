#!/usr/bin/env python

import sys
import random
from timeit import timeit

from bubblesort    import bubblesort
from mergesort     import mergesort
from quicksort     import quicksort
from insertionsort import insertionsort
from gnomesort     import gnomesort
from selectionsort import selectionsort
from heapsort      import *

#elements = sys.argv[1:]
## we need ints, not strings
#elements = list(map(int, elements))

elements = [ random.randint(1,20) for _ in range(20) ]

print(elements)
print(bubblesort(elements[:]))
print(mergesort(elements[:]))
print(quicksort(elements[:]))
print(insertionsort(elements[:]))
print(gnomesort(elements[:]))
print(selectionsort(elements[:]))
print(heapsort(elements[:]))
