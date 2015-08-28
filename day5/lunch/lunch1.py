#!/usr/bin/env python

'''
Print sequence name, identity ratio, and gap ratio
'''

import sys

align_file = open("/Users/cmdb/qbb2015-homework/day5/lunch/alignment.txt")

while 1:
    line = align_file.readline()
    if line.startswith( ">" ) or line.startswith(" Identities"):
        print line.lstrip( ">").rstrip("\r\n")
    elif line. startswith ("~"):
        break
    else:    
        pass
    
    





