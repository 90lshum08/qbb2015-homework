#!/usr/bin/env python

'''
SYNTAX: ./lunch1.py sys.argv[1,2,3,4]
    argv[1] : .len file
    argv[2] : ignore this, type nonsense
    argv[3] : .bed file - first protein alignment (CTCF)
    argv[4] : desired alignment percentage as float
    argv[5] : .bed file - second protein alignment (BEAF)
    argv[6] : desired alignment percentage as float
    argv[7] : .bed file - third alignment protein (Su(HW))
    argv[8] : desired alignment percentage as float

'''
from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import sys
import fileinput
import copy
from matplotlib_venn import venn3, venn3_circles

def arrays_from_len_file( fname ):
    arrays = {}
    for line in open( fname ):
        fields = line.split()
        # In the len file, the first column is the chromosome name
        name = fields[0]
        # In the len file, the second column is the chromosome length
        size = int( fields[1] )
        # This will store the data as a boolean array. We only need to know if the gene was marked yes or no. np.zeros fills the array with zeros = size
        arrays[ name ] = np.zeros( size, dtype = bool )
    # A function will nut soit out any data unless you tell it to return something    
    return arrays
    
def set_bits_from_file( arrays, fname ):
    for line in open( fname ):
        fields = line.split()
        # Parse fields
        chromosome = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        # This takes every zero int the original array and turns it to a 1 if it falls between where a gene is marked (start:end)
        arrays[ chromosome ][ start : end ] = 1


phastA= arrays_from_len_file( sys.argv[1] )
set_bits_from_file ( phastA, sys.argv[3] )

phastB= arrays_from_len_file( sys.argv[1] )
set_bits_from_file ( phastB, sys.argv[5] )

phastC= arrays_from_len_file( sys.argv[1] )
set_bits_from_file ( phastC, sys.argv[7] )


A = 0
B = 0
C = 0
AB = 0
AC = 0
BC = 0
ABC = 0

percent1 = float( sys.argv[4] )
percent2 = float( sys.argv[6] )
percent3 = float (sys.argv[8] )


for x in [3,5,7]:
    file = open(sys.argv[x])
    for line in file:
        fields = line.split()
        # Parse fields
        chromosome = fields[0]
        start = int( fields[1] )
        end = int( fields[2] )
        # Get slice
        slA = phastA[ chromosome ][ start : end ]
        slB = phastB[ chromosome ][ start : end ]
        slC = phastC[ chromosome ][ start : end ]

        if ( np.sum (slA) / len( slA ) > percent1 ) == True and ( np.sum (slB) / len( slB ) > percent2 ) == False and ( np.sum (slC) / len( slC ) > percent3 ) == False:
            A += 1
        elif ( np.sum (slA) / len( slA ) > percent1 ) == False and ( np.sum (slB) / len( slB ) > percent2 ) == True and ( np.sum (slC) / len( slC ) > percent3 ) == False:
            B += 1
        elif ( np.sum (slA) / len( slA ) > percent1 ) == False and ( np.sum (slB) / len( slB ) > percent2 ) == False and ( np.sum (slC) / len( slC ) > percent3 ) == True:
            C += 1
        elif ( np.sum (slA) / len( slA ) > percent1 ) == True and ( np.sum (slB) / len( slB ) > percent2 ) == True and ( np.sum (slC) / len( slC ) > percent3 ) == False:
            AB += 1
        elif ( np.sum (slA) / len( slA ) > percent1 ) == True and ( np.sum (slB) / len( slB ) > percent2 ) == False and ( np.sum (slC) / len( slC ) > percent3 ) == True:
            AC += 1
        elif ( np.sum (slA) / len( slA ) > percent1 ) == False and ( np.sum (slB) / len( slB ) > percent2 ) == True and ( np.sum (slC) / len( slC ) > percent3 ) == True:
            BC += 1
        elif ( np.sum (slA) / len( slA ) > percent1 ) == True and ( np.sum (slB) / len( slB ) > percent2 ) == True and ( np.sum (slC) / len( slC ) > percent3 ) == True:
            ABC += 1
        else:
            #print "pass"
            pass
                
print A
print B
print C
print AB
print AC
print BC
print ABC

plt.figure()
v = venn3( subsets = (A, B, AB , C, AC , BC , ABC ), set_labels = ("CTCF", "BEAF", "Su(HW)"))   
plt.savefig("CTCF_BEAF_SuHWvenn.png")  

