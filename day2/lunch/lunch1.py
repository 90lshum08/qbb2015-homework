#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/BDGP6.SAM"

file = open( filename )
alignment_count = 0

for data in file:
    line = data.split()
    
    if line[0] != "@SQ":
        alignment_count +=1
    else:
        pass
        
print alignment_count - 1
    
    