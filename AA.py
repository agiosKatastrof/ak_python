#!/usr/bin/python
'''
j = int(raw_input())
i = raw_input()
'''
j = 5
#i = '1 3 5 9 11'
i = '1 5 7 9 11'

numbers = i.split(" ")

deltas = {}

for i in range(0,j):
    prev = int(numbers[i-1])
    current = int(numbers[i])
    delta = current - prev
    deltas[i] = delta
    
    print "Current ", current
    print "Delta ", delta
    
    if delta > 0 and deltas[i-1] > 0:
        if delta > deltas[i-1]:
            print current - deltas[i-1]
            break
        elif delta < deltas[i-1]:
            print prev - delta
            break
        pass
        
    print
        
print deltas

    
    
 
