#!/usr/bin/python

import random

list = []
for i in range(1,11):
    list.append(random.randint(0,100))
    
print list

def qsort(alist):
    
    if len(alist) == 0:
        return alist
    
    else:
        p = alist.pop(0)
        print "P ", p
        slist = []
        left = []
        right = []
  
        for i in alist:
            if i < p:
                left.append(i)
            else:
                right.append(i)
        
        slist = qsort(left) + [p] + qsort(right)
    
        print "L %d" % len(left), left
        print "R %d" % len(right), right
        
    return slist


print qsort(list)