#!/usr/bin/python

list = [1,2,3,5]

iterator = iter(list)

for i in range(1,10):
    i += 1
    print iterator.next()