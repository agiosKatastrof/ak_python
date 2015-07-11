class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.nxt = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.nxt

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnxt):
        self.nxt = newnxt
