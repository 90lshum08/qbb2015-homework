#!/usr/bin/env python

'''
Plot histogram or score and e values, and a scatterplot relating them
'''

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

align_file = pd.read_table("/Users/cmdb/qbb2015-homework/day5/lunch/tabalignment.txt")
score = align_file["Score"]
evalue = align_file["E"]

evallog = - np.log10(evalue)
scorelog = np.log10(score)

plt.figure()
plt.title("E value vs Score")
plt.plot(scorelog, evallog, 'o')
plt.xlabel("log Score")
plt.ylabel("-log E value")
plt.savefig("scatterEvsScore.png")