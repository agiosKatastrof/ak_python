#!/usr/bin/python

from Graph import Graph
from Queue import Queue
from Vertex import Vertex


def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile,'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        print word
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g
        
        
def bfs(g,start):
  start.setDistance(0)
  start.setPred(None)
  vertQueue = Queue()
  vertQueue.enqueue(start)
  while (vertQueue.size() > 0):
    currentVert = vertQueue.dequeue()
    print 'Current ', currentVert.id
    for nbr in currentVert.getConnections():
      if (nbr.getColor() == 'white'):
        nbr.setColor('gray')
        nbr.setDistance(currentVert.getDistance() + 1)
        nbr.setPred(currentVert)
        vertQueue.enqueue(nbr) 
    currentVert.setColor('black')
    
def traverse(x):
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())
    
    
g = buildGraph('wordFile.txt')

start = g.getVertex('DOPE')

for c in start.getConnections():
    print "Conn " , c.id

bfs(g,start)

print "new"
traverse(g.getVertex('NOPE'))
#print g.getVertices()

