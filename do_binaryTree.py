#!/usr/bin/python

from BinaryTree import BinaryTree


r = BinaryTree('a')
r.insertLeft('b')
r.getLeftChild().insertRight('d')

print r.getLeftChild().getRightChild().getRootVal()
