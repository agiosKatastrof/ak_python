#!/usr/bin/python

import sys

infile, outfile = sys.argv[1], sys.argv[2]

print infile, outfile

in_file = open(infile,'r')
out_file = open(outfile,'a')

for line in in_file.readlines():
    a = line.split(',')[0]
    b = line.split(',')[1]
    
    out =  "%s %s" % (a,b)
    out_file.write(out)

in_file.close()
out_file.close()
    