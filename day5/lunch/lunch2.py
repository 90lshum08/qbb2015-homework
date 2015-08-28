#!/usr/bin/env python

'''
Plot histogram or score and e values, and a scatterplot relating them
'''

import sys
import pandas as pd
import matplotlib.pyplot as plt

align_file = pd.read_table("/Users/cmdb/qbb2015-homework/day5/lunch/tabalignment.txt")
score = align_file["Score"]
evalue = align_file["E"]

print score, evalue 

plt.figure()
plt.title("Score")
plt.hist(score, bins = 100, range = (0, 100))
plt.xlabel("Score")
plt.ylabel("Score Frequency")
plt.savefig("scorehist.png")
plt.figure()
plt.title("E Values")
plt.hist(evalue, bins = 200, log = True)
plt.xlabel("log E value")
plt.ylabel("lof Ferquency")
plt.savefig("evaluehist.png")

