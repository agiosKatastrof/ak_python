#!/usr/bin/python

from BinHeap import BinHeap

l = [9, 5, 6, 2, 3]
b = BinHeap()

b.buildHeap(l)

print b.currentSize
print b.heapList

print b.delMin()

print b.heapList

b.insert(7)

print b.heapList

print b.delMax()

print b.heapList