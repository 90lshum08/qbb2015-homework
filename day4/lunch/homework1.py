#!/usr/bin/env python
'''
Create a venn the compares the unions of 3 bed files
        sys.argv[1] : len file
        sys.argv[2,3,4] : bed files to conpare
'''
from __future__ import division
import matplotlib.pyplot as plt
import sys
import chrombits
from matplotlib_venn import venn3, venn3_circles
import fileinput
import copy


arr=chrombits.ChromosomeLocationBitArrays(sys.argv[1])


A_arr = copy.deepcopy(arr)
B_arr = copy.deepcopy(arr)
C_arr = copy.deepcopy(arr)

A_arr.set_bits_from_file(sys.argv[2])
B_arr.set_bits_from_file(sys.argv[3])
C_arr.set_bits_from_file(sys.argv[4])

A_arr.Start_End_Bed(sys.argv[2])
B_arr.Start_End_Bed(sys.argv[3])
C_arr.Start_End_Bed(sys.argv[4])

union_table = A_arr.union(B_arr).union(C_arr)

print union_table


plt.fig()
v = venn3(subsets = union_table, set_labels = ("CTCF, BEAF, Su(HW)"))
plt.savefig("union_venn.png")