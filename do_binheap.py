#!/usr/bin/python

import random

from BinHeap import BinHeap

left = BinHeap()
right = BinHeap()

numbers = []
median = 0

def mean2(a,b):
    return (a.returnMax() + b.returnMin())/2.0

for n in range(1,10):
 #   i = random.randint(0,100)
    i = n
    numbers.append(i)
    if len(numbers) == 1:
        median = i
        left.insert(i)
    elif len(numbers) == 2:
        if i > left.returnMax():
            right.insert(i)
        else:
            right.insert(left.returnMax())
            left.delMax()
            left.insert(i)
        median = mean2(left,right)
    else:
        if left.currentSize < right.currentSize:
            if i <= right.returnMin():
                left.insert(i)
            else: #  i > right.returnMin():
                rightMin = right.returnMin()
                right.delMin()
                right.insert(i)
                left.insert(rightMin)
            median = mean2(left,right)
        elif left.currentSize > right.currentSize:
            if i >= right.returnMin():
                right.insert(i)
            else: # i < right.returnMin()
                leftMax = left.returnMax()
                left.delMax()
                left.insert(i)
                right.insert(leftMax)
            median = mean2(left,right)
        else: # left and right have same size
            if i > left.returnMax() and i < right.returnMin():
                median = i
                left.insert(i)
            elif i < left.returnMax():
                left.insert(i)
                median = left.returnMax()
            else: # i > right.returnMin()
                right.insert(i)
                median = right.returnMin()

                
    
    print "I: ", i
    print "M: %.1f" % median
    print numbers


    print

    