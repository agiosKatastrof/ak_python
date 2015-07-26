#!/usr/bin/python

import threading
import time
import logging

logging.basicConfig(level =logging.DEBUG, format = 'HELLO %(message)s %(levelname)s %(threadName)-10s',)

def worker(x):
    print threading.currentThread().getName(), 'Starting'
    print "doing work for ", x
    logging.debug('Check this out')
    print
    
    time.sleep(10.0)
    print threading.currentThread().getName(), 'Exiting'
    print
    return

threads = []

for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    #threads.append(t)
    t.start()
    #print threads
    print threading.activeCount(), "kids alive"
    print threading.enumerate()
    t.join(1.0)
    if t.isAlive():
        print t.name, "is Alive"
        try:
            print "try to stop ", t.name
            thread._Thread_stop()
        except:
            print "Could not stop ", t.name
    print t.name, "is now ", t.isAlive()
    print "PARENT SEES THAT YOU ARE DONE: ", t.name
    
    
#t1 = threading.Thread(name="SP", target=worker, args=('special',))
#t1.start()