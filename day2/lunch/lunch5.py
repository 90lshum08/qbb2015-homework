#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/genomes/BDGP6.SAM"

file = open( filename )
chromosome_counts={}

for data in file:
    fields = data.split()
    chromosome_name = fields[2]
    
    if chromosome_name not in chromosome_counts and (chromosome_name == "2L" or chromosome_name == "2R" or chromosome_name == "3L" or chromosome_name == "3R" or chromosome_name ==  "4" or chromosome_name ==  "X"):
        chromosome_counts[ chromosome_name ] = 1
    elif chromosome_name in chromosome_counts:
        chromosome_counts[ chromosome_name ] += 1
    else:
        pass

for key, value in chromosome_counts.iteritems():
    print key, value
    
        