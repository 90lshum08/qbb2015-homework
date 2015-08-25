#!/usr/bin/env python

# For first 10 lines, report Chromosome Name. Report "RNAME", 3rd column

filename = "/Users/cmdb/qbb2015/genomes/BDGP6.SAM"

file = open( filename )
line_count = 0
for data in file:
    fields = data.split()
    chromosome_name = fields[2]
    
    if "@" not in fields[0] :
       print chromosome_name
       line_count += 1
       
    if line_count == 10 :
        break

