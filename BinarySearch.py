class BinarySearch(object):
    def __init__(self):
        pass

    def binSearch(self,alist,item):
        found = False
        first = 0
        last = len(alist) -1
        midpoint = 0
        
        while first <= last and not found:
            midpoint = (first + last)//2
            print midpoint
            if alist[midpoint] == item:
                found = True
            else:
                if item < alist[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
                    
        return found
        


