#!/usr/bin/python

import random

from BinHeap import BinHeap

left = BinHeap()
right = BinHeap()

numbers = []
median = 0

incoming = [1,9,1,2,5,10,1]

def mean2(a,b):
    return (a.returnMax() + b.returnMin())/2.0

for n in incoming:
 #   i = random.randint(0,10)
    i = n
    numbers.append(i)
    
    print "I: ", i
    print "L size: ", left.currentSize
    print "R size: ", right.currentSize
    print "L max: ", left.returnMax()
    print "R min: ", right.returnMin()
    
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
            if i <= left.returnMax():
                left.insert(i)
            else: # i > left.returnMax():
                right.insert(i)
                rightMin = right.returnMin()
                right.delMin()
                left.insert(rightMin)
            median = mean2(left,right)
        elif left.currentSize > right.currentSize:
            if i >= right.returnMin():
                right.insert(i)
            else: # i < right.returnMin()
                left.insert(i)
                leftMax = left.returnMax()
                left.delMax()
                right.insert(leftMax)
            median = mean2(left,right)
        else: # left and right have same size
            if i > left.returnMax() and i < right.returnMin():
                left.insert(i)
                median = i
            elif i <= left.returnMax():
                print  "YOO"
                print "LMAX-: ", left.returnMax()
                print "I: ", i
                print "SIZE- ", left.currentSize
                left.insert(i)
                print "SIZE ", left.currentSize
                print "LMAX: ", left.returnMax()
                median = left.returnMax()
            else: # i >= right.returnMin():
                right.insert(i)
                median = right.returnMin()

                
    
    print "M: %.1f" % median
    print "L+ size: ", left.currentSize
    print "R+ size: ", right.currentSize
    print "L+ max: ", left.returnMax()
    print "R+ min: ", right.returnMin()

    print numbers
    numbers.sort()
    print numbers


    print

    