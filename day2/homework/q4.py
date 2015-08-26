#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab"
f= open(annotation)

df = pd.read_table(f)

fpkm_df=df[df.FPKM !=0]
fpkm=fpkm_df["FPKM"]

line_count=0
for line in fpkm:
    line_count +=1

one=line_count/3 + 1
two=2*line_count/3 + 1
three=line_count + 1


First=fpkm[0:one].values
Middle=fpkm[one:two].values
Last=fpkm[two:three].values

region_count=1
for region in [First, Middle, Last]:
    plt.figure()
    plt.title("Region" + str(region_count))
    plt.boxplot(region)
    plt.savefig("Region" + str(region_count) + ".png")
    region_count += 1

        

    


