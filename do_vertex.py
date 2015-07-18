#!/usr/bin/python

from Vertex import Vertex
from Graph import Graph

a = Vertex('a')
b = Vertex('b')
c = Vertex('c')

a.addNeighbor(b)
a.addNeighbor(c,100)

for v in a.getConnections():
    print v

print a.getId()

print a.getWeight(b)
print a.getWeight(c)

print "ME: " , a

g = Graph()
for i in range(6):
    g.addVertex(i)


g.addEdge(1,2,10)

for vtx in g:
    for conn in vtx.getConnections():
        print "%s, %s" % (vtx.getId(), conn.getId() )