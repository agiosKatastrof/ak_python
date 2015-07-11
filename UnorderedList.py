from Node import Node

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else :
                current =  current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
           self.head = current.getNext()
        else:
          previous.setNext(current.getNext())

    def getLast(self):
        current = self.head
        while current.nxt != None:
            current = current.getNext()

        return current

    def printList(self):
        current = self.head
        while current.nxt != None:
            print current.getData()
            current = current.getNext()
        print current.getData()

    def append(self,item):
        last = self.getLast()
        newLast = Node(item)
        last.setNext(newLast)

    def pop(self):
        last = self.getLast()
        self.remove(last.getData())

        return last

    def index(self,item):
        current = self.head
        found = False
        n = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                print n
                n += 1

        return n

    def insert(self,item,idx):
        current = self.head
        n = 0
        while n < idx:
            current = current.getNext()
            n += 1

        insertee = Node(item)
        nxt = current.getNext()
        current.setNext(insertee)
        insertee.setNext(nxt)




