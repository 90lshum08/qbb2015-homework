#!/usr/bin/env python

# Find perfect matches in sam file. Look for "NM:i:0"

filename = "/Users/cmdb/qbb2015/genomes/BDGP6.SAM"

file = open( filename )
perfect_count=0

for data in file:
    
    if "NM:i:0" in data:
        perfect_count +=1
    else:
        pass
        
print perfect_count
