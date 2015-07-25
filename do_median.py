#!/usr/bin/python

from heapq import *

left = []
right = []

numbers = []
median = 0

incoming = [1,9,1,2,5,10,1,0,8]

def getMin(heap):
    # just return the min from the heap
    if len(heap) > 0:
        return nsmallest(1,heap)[0]
    else:
        return "N/A"

def delMin(heap):
    # returns min, removes min from heap
    return heappop(heap)

def getMax(heap):
    # just return the max from the heap
    if len(heap) > 0:
        return nlargest(1,heap)[0]
    else:
        return "N/A"

def delMax(heap):
    # returns max, removes max from heap
    m = nlargest(1,heap)[0]
    i = heap.index(m)
    return heap.pop(i)

def med(l,r):
    if len(l) > len(r):
        return getMax(l)
    elif len(l) < len(r):
        return getMin(r)
    else: # len(l) == len(r):
        return (getMax(l) + getMin(r))/2.0


print "Original: ", incoming
print

for i in incoming:
    print "Incoming: ", i
    numbers.append(i)
    print "Left- ", left
    print "Left Max", getMax(left)
    print "Right- ", right
    print "Right Min", getMin(right)
    
    if len(numbers) == 1:
        median = i
        heappush(left,i)
    elif len(numbers) == 2:
        if i > getMax(left):
            heappush(right,i)
        else:
            j = delMax(left)
            heappush(right,j)
            heappush(left,i)
        median = med(left,right)
    else:
        if len(left) == len(right):
            if i <= getMax(left):
                heappush(left,i)
            else: #i > getMax(left):
                heappush(right,i) 
        elif len(left) > len(right):
            if i > getMax(left) and i <= getMin(right):
                heappush(right,i)
            else: # i <= getMax(left)
                heappush(left,i)
                leftMax = delMax(left)
                heappush(right,leftMax)
        else: # len(left) < len(right):
            if i <= getMax(left) and i < getMin(right):
                heapush(left,i)
            else: # i > getMax(left)
                heappush(right,i)
                rightMin = delMin(right)
                heappush(left,rightMin)
               
        median = med(left,right)    

    print "Left", left
    print "MEDIAN", median
    print "Right", right
    numbers.sort()
    print "List", numbers
    print
    

