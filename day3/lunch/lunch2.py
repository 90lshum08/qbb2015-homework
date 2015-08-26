#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")

fpkm_df = df[df.FPKM !=0]
FPKM = fpkm_df["FPKM"]

fpkm =[]

for line in FPKM:
    fpkm.append(line)

plt.figure()
plt.title("FPKM")
plt.hist(fpkm, bins =range(len(fpkm)), log=True)
plt.savefig("fpkmhistogram.png")


