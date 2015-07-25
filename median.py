#!/usr/bin/python

import random

m = 0
left = 0
right = 0
numbers = []

def median(n,m):
    numbers.append(n)
    lenN = len(numbers)
    if lenN > 1:
        if lenN % 2 > 0:
            pass
        else:
            pass
    else:
        m = n
        
    return m



for i in range(0,10):
    n = (random.randint(0,1000))
    m = median(n,m)
    print "%d %d %d" % (left, m, right)
    
print numbers


    














