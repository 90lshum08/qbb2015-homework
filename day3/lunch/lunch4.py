#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats as st
import numpy as np

seqdf = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072901/t_data.ctab")
repdf = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072902/t_data.ctab")

#seqno = seqdf[seqdf.FPKM !=0]
#repno = repdf[repdf.FPKM !=0]

seq = seqdf["FPKM"]
rep = repdf["FPKM"]



# 0=FPKM of seq, 1=FPKM of rep, 2=1-0, 3= 1+2
Data = [[], [], [], []]

for line in seq:
    Data[0].append(line)
    
for line in rep:
    Data[1].append(line)

for number in range(0, len(Data[1])):
    Data[2].append((np.log2(Data[1][number]) - np.log2(Data[0][number])))
    Data[3].append(((np.log2((Data[1][number]) + np.log2(Data[0][number])))/2))
    
M = Data[2]
A = Data[3]

plt.figure()
plt.title("MA of 901 vs 902")
plt.plot(A, M, 'o')
plt.xlabel("A")
plt.ylabel("M")
plt.savefig("MAplot901to902.png")


