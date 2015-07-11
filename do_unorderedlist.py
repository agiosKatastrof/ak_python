#!/usr/bin/python

import random
from UnorderedList import UnorderedList

myList = UnorderedList()

for i in range(1,11):
    n = random.randint(1,100)
  #  print "%d> %d" % (i,n)
    myList.add(n)

myList.add(12)
myList.add(24)

print myList.size()
print "search", myList.search(12)

print "last: %d" % myList.getLast().getData()

myList.printList()

myList.append(40)

print
myList.printList()
print


print "idx %d, %d" % (12, myList.index(12))

print "last", myList.pop().getData()

print "insert", myList.insert(100,2)

myList.printList()
