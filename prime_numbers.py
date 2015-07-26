#!/usr/bin/python

import sys
import os

def getNumberOfPrimes(n):
    
    primes = {}
    for i in range(2,n+1):
        if i % 2 > 0:
            primes[i] = True
        else:
            if i == 2:
                primes[i] = True
            else:
                primes[i] = False

    for i in range(3,n+1):
        if primes[i] == True:
            j = 2*i
            while j <= n+1:
                j += i
                primes[j] = False
    count = 0            
    for p in primes:
        if primes[p] == True:
            count += 1
            
    return count


print getNumberOfPrimes(100)
    