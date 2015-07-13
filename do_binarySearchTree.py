#!/usr/bin/python

from BinarySearchTree import BinarySearchTree

bst = BinarySearchTree()

bst.put(10,'a')
bst.put(9,'b')
bst.put(2,'c')
bst.put(12,'d')
bst.put(14,'e')
bst.put(11,'e')
bst.put(16,'e')

bst[20] = 'f'
print bst.length()


print  bst.get(12)
print  bst.get(20)

bst.delete(12)

bst.delete(2)
print

for i in bst:
    print i