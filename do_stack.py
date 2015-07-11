#!/usr/bin/python

from Stack import Stack

import sys

print sys.version

stack = Stack()

print "size: %s" % stack.size()

stack.push('foo')
stack.push('boo')

print "size again: %s" % stack.size()
print "peek %s" % stack.peek()

print "pop %s" % stack.pop()
