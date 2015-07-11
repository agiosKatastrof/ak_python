#!/usr/bin/python

import sys
from Deque import Deque

deque = Deque()

print  deque.size();
deque.addFront('a')
deque.addFront('b')
deque.addRear('c')
deque.addRear('e')

print deque.removeRear()
print deque.removeFront()

