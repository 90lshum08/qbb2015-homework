#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/BDGP6.SAM"

file = open( filename )
MAPQtotal=0
MAPQcount=0


for data in file:
    fields = data.split()
    
    if "@" not in fields[0] :
        field2 = data.split()
        field2_as_int = int( field2[4] )
        MAPQtotal = MAPQtotal + field2_as_int
    
        MAPQcount += 1
    else:
        pass

print MAPQtotal/MAPQcount

    