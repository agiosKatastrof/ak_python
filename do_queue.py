#!/usr/bin/python

import sys
from Queue import Queue

print sys.version

queue = Queue()

print "size: %d" % queue.size()

queue.enqueue('foo')
queue.enqueue('boo')
queue.enqueue('noo')

print "size: %d" % queue.size()

print queue.dequeue()

print queue.isEmpty()
print queue.size()

