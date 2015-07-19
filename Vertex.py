class Vertex(object):
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.distance = None
        self.pred = None
        self.color = 'white'
        
    def setDistance(self,d):
        self.distance = d
        
    def setPred(self,p):
        self.pred = p
        
    def setColor(self,c):
        self.color = c
        
    def getDistance(self):
        return self.distance
    
    def getPred(self):
        return self.pred
    
    def getColor(self):
        return self.color
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def __str__(self):
        return str(self.id) + ' connectedTo: '  + str([x.id for x in self.connectedTo])
       
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]

