#!/usr/bin/python

from BinaryTree import BinaryTree


r = BinaryTree(10)
r.insertLeft(5)
r.getLeftChild().insertRight(6)
r.insertRight(15)
r.getRightChild().insertLeft(11)
r.getRightChild().insertRight(100)

print r.getRootVal()
print r.getLeftChild().getRootVal()
print r.getLeftChild().getRightChild().getRootVal()
print r.getRightChild().getRootVal()
print r.getRightChild().getLeftChild().getRootVal()
print r.getRightChild().getRightChild().getRootVal()

print

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

preorder(r)
print
r.preorder()
print
r.postorder()
print
r.inorder()
