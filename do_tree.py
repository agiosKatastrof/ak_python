#!/usr/bin/python

from Tree import Tree

myTree = Tree()

x = myTree.BinaryTree('a')
print x
myTree.insertLeft(x,'b')
print x
myTree.insertRight(x,'c')
print x

myTree.insertRight(myTree.getRightChild(x),'d');

print x

myTree.insertLeft(myTree.getRightChild(myTree.getRightChild(x)),'e')

print x
