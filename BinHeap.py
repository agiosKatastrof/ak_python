class BinHeap(object):
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def percUp(self,i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:  # you get the parent by i // 2
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i] # swap parent with child
                self.heapList[i] = tmp
            i = i // 2
    
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)
        
    def percDown(self,i):
        while (i * 2) <= self.currentSize: # you get the child by i * 2
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]: # swap child with parent
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = i * 2
            
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize: # no right child
            return i * 2  # so return left child
        else:
            if self.heapList[i*2] < self.heapList[i*2 + 1]:
                return i * 2   # return left child
            else:
                return i * 2 + 1 # return right child
            
    def delMin(self):
        retval = self.heapList[1] # the root node is always the min in a bin heap
        self.heapList[1] = self.heapList[self.currentSize] # make the last node the root node
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval
   
    def delMax(self):
        retval = None
        rLast = self.heapList[self.currentSize]
        rLastMinusOne = self.heapList[self.currentSize - 1]
        
        if rLast >= rLastMinusOne:
            retval = rLast
        else:
            retval = rLastMinusOne
            tmp = self.heapList[self.currentSize]
            self.heapList[self.currentSize - 1] = tmp
        
        self.heapList.pop(self.currentSize)    
        self.currentSize -= 1
        return retval

        
        
    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i -= 1
            
            
        
        
