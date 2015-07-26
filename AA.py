#!/usr/bin/python

j = int(raw_input())
i = raw_input()

#j = 5
#i = '1 11 31 41 51'
#i = '1 3 5 9 11'
#i = '5 4 3 2 0'
#i = '5 3 2 1 0'

numbers = i.split(" ")

deltas = {}

for i in range(0,j):
    prev = int(numbers[i-1])
    current = int(numbers[i])
    delta = current - prev
    deltas[i] = delta
    
  #  print "Current ", current
 #   print "Delta ", delta
    

    if i > 1:
        if abs(delta) > abs(deltas[i-1]):
            print current - deltas[i-1]
            break
        if abs(delta) < abs(deltas[i-1]):
            print prev - delta
            break
        
   # print
        
#print deltas

    
    
 
