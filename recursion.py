#!/usr/bin/python

list = [1,2,5,6,11,10]

def lsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        print numList
        return numList[0] + lsum(numList[1:])


print lsum(list)

