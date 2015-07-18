#!/usr/bin/python

from LocalMaxima import LocalMaxima

data = [10,9,7,5,6,3,5,6,12,12,12,11]

def find(list):
    maxima = []
    for i in range(0,len(list)):
        print i
        if i == 0:
            if list[i] >= list[i+1]:
                maxima.append(i)
        elif i == len(list)-1:
            if list[i] >= list[i-1]:
                maxima.append(i)
            pass
        else:
            if (list[i] >= list[i-1]) and (list[i] >= list[i+1]):
                maxima.append(i)
        
    return maxima


max = find(data)
print max
for i in max:
    print data[i]

