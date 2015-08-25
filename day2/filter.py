#!/usr/bin/env python

filename = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"

f = open( filename )

for data in f:
    # Split the line on whitespace
    fields = data.split()
    # Determine if the 9th column contains the string "tRNA"
    if "tRNA" in fields[9]:
        # The comma at the end suppresses the line, so that the output isn't double spaced
        print data,

