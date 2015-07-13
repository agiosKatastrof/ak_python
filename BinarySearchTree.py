from TreeNode import TreeNode

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size += 1
        
    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,val,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,val,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,val,parent=currentNode)
    
    def __setitem__(self,k,v):
        self.put(k,v)
        
    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    def _get(self,key,currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __contains__(self,key):
        if self.__get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')
        
    def __delitem__(self,key):  
        self.delete(key)
        
    def remove(self,currentNode):
        print "Remove ", currentNode.key
        if currentNode.isLeaf():
            print "It's a leaf node on %d with parent %d" % (currentNode.key, currentNode.parent.key)
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        elif currentNode.hasLeftChild() and not currentNode.hasRightChild():
            if currentNode.isLeftChild():
                currentNode.leftChild.parent = currentNode.parent.leftChild
                currentNode.parent.leftChild = currentNode.leftChild
            elif currentNode.isRightChild():
                currentNode.leftChild.parent = currentNode.parent.rightChild
                currentNode.parent.rigthChild = currentNode.leftChild
            else: # currentNode is root
                currentNode.replaceNodeData(currentNode.leftChild.key,
                                            currentNode.leftChild.payload,
                                            currentNode.leftChild.leftChild,
                                            currentNode.leftChild.rigthChild)
        elif currentNode.hasRightChild() and not currentNode.hasLeftChild():
            if currentNode.isLeftChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.leftChild = currentNode.rightChild
            elif currentNode.isRightChild():
                currentNode.rightChild.parent = currentNode.parent
                currentNode.parent.rightChild = currentNode.rightChild
            else: # currentNode is root
                currentNode.replaceNodeDatea(currentNode.rightChild.key,
                                             currentNode.rightChild.payload,
                                             currentNode.rightChild.leftChild,
                                             currentNode.rigthChild.rigthChild)
        else: # has both nodes
            pass
                
        
                    