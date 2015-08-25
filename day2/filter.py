#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open( filename )

# Iterate the file line by line
for line_count, data in enumerate( f ):
    # If line_count is below 10,do nothing
    if line_count <= 10:
        pass
    # If line_count is between 11 and 15, print
    elif line_count <= 15:
        print data,
    # Don't read the entire document    
    else:
        break
