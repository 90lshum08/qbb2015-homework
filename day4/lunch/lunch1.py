#!/usr/bin/env python

'''
SYNTAX: ./lunch1.py sys.argv[1,2,3,4]
    argv[1] : .len file
    argv[2] : ignore this, load a random file
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

        # if slA.all() == True and slB.all() == False and slC.all() == False:
        #     A += 1
        # elif slA.all() == False and slB.all() == True and slC.all() == False:
        #     B += 1
        # elif slA.all() == False and slB.all() == False and slC.all() == True:
        #     C += 1
        # elif slA.all() == True and slB.all() == True and slC.all() == False:
        #     AB += 1
        # elif slA.all() == True and slB.all() == False and slC.all() == True:
        #     AC += 1
        # elif slA.all() == False and slB.all() == True and slC.all() == True:
        #     BC += 1
        # elif slA.all() == True and slB.all() == True and slC.all() == True:
        #     ABC += 1
        # else:
        #     pass
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
v = venn3( subsets = (A, B, int(AB/2) , C, int(AC/2) , int(BC/2) , int(ABC/3) ), set_labels = ("CTCF", "BEAF", "Su(HW)"))   
plt.savefig("CTCF_BEAF_SuHWvenn.png")  









'''
pro1_array = arrays_from_len_file( sys.argv[1] )
set_bits_from_file ( phast, sys.argv[2])
set_bits_from_file ( pro1_array, sys.argv[3])

pro2_array = arrays_from_len_file( sys.argv[1] )
set_bits_from_file ( phast, sys.argv[2])
set_bits_from_file ( pro2_array, sys.argv[5])

pro3_array = arrays_from_len_file( sys.argv[1] )
set_bits_from_file ( phast, sys.argv[2])
set_bits_from_file ( pro3_array, sys.argv[3])        
set_bits_from_file ( pro3_array, sys.argv[5])

# Total CTCF
overlap_pro1 = 0
pro1_percent = float( sys.argv[4] )
for line in open( sys.argv[3] ):
    fields = line.split()
    # Parse fields
    chromosome = fields[0]
    start = int( fields[1] )
    end = int( fields[2] )
    # Get slice
    sl1 = phast[ chromosome ][ start : end ]
    # Aggregate
    overlap_pro1 += ( np.sum (sl1) / len( sl1 ) > pro1_percent )
    #array_percent1 = { }
   # array_percent1[ start : end ].extend( sl1 )

#print array_percent1
# Total BEAF       
overlap_pro2 = 0
pro2_percent = float( sys.argv[6] )
for line in open( sys.argv[5] ):
    fields = line.split()
    # Parse fields
    chromosome = fields[0]
    start = int( fields[1] )
    end = int( fields[2] )
    # Get slice
    sl2 = phast[ chromosome ][ start : end ]
    # Aggregate
    overlap_pro2 += ( np.sum (sl2) / len( sl2 ) > pro2_percent )

# Total Su(HW)   
overlap_pro3 = 0
pro3_percent = float( sys.argv[8] )
for line in open( sys.argv[7] ):
    fields = line.split()
    # Parse fields
    chromosome = fields[0]
    start = int( fields[1] )
    end = int( fields[2] )
    # Get slice
    sl3 = phast[ chromosome ][ start : end ]
    # Aggregate
    overlap_pro3 += ( np.sum (sl3) / len( sl3 ) > pro3_percent )

# Total CTCF and BEAF    
overlap_pro12 = 0
pro12_percent = float( sys.argv[9] )
for line in open( sys.argv[5] ):
    fields = line.split()
    chromosome = fields[0]
    start = int( fields[1] )
    end = int( fields[2] )
    sl12 = pro1_array[ chromosome ][ start : end ]
    overlap_pro12 += ( np.sum (sl12) / len(sl12) > pro12_percent )

# Total CTCF and Su(HW)    
overlap_pro13 = 0
pro13_percent = float( sys.argv[10] )
for line in open( sys.argv[7] ):
    fields = line.split()
    chromosome = fields[0]
    start = int( fields[1] )
    end = int( fields[2] )
    sl13 = pro1_array[ chromosome ][ start : end ]
    overlap_pro13 += ( np.sum (sl13) / len(sl13) > pro13_percent )
    
# Total CTCF and Su(HW)    
overlap_pro23 = 0
pro23_percent = float( sys.argv[11] )
for line in open( sys.argv[7] ):
    fields = line.split()
    chromosome = fields[0]
    start = int( fields[1] )
    end = int( fields[2] )
    sl23 = pro2_array[ chromosome ][ start : end ]
    overlap_pro23 += ( np.sum (sl23) / len(sl23) > pro23_percent )

# Total CTCF and Su(HW)    
overlap_pro123 = 0
pro123_percent = float( sys.argv[12] )
for line in open( sys.argv[7] ):
    fields = line.split()
    chromosome = fields[0]
    start = int( fields[1] )
    end = int( fields[2] )
    sl123 = pro3_array[ chromosome ][ start : end ]
    overlap_pro123 += ( np.sum (sl123) / len(sl123) > pro123_percent )

only1 = ( overlap_pro12 - overlap_pro123 ) - (overlap_pro13 - overlap_pro123 ) - overlap_pro123
only2 = ( overlap_pro12 - overlap_pro123 ) - (overlap_pro23 - overlap_pro123 ) - overlap_pro123
only3 = ( overlap_pro13 - overlap_pro123 ) - (overlap_pro23 - overlap_pro123 ) - overlap_pro123
both12 = overlap_pro12 - overlap_pro123
both13 = overlap_pro13 - overlap_pro123
both23 = overlap_pro23 - overlap_pro123

plt.figure()
plt.title("Overlap CTCF, BEAF, Su(HW)")
v = venn3( subsets = ( only1, only2, both12, only3, both13, both23, overlap_pro123), set_labels = ("CTCF", "BEAF", "Su(HW)" ) )
plt.show()
'''