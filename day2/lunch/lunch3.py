#!/usr/bin/env python

# Find number of times a sequence hits once (matches one genome). Look for "NH:i:1"

filename = "/Users/cmdb/qbb2015/genomes/BDGP6.SAM"

file = open( filename )
hit_count=0

for data in file:
    
    if "NH:i:1" in data:
        hit_count +=1
    else:
        pass
        
print hit_count