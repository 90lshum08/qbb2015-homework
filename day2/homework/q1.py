#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header = None)
df.columns = ["Chromosome", "Database", "Type", "Start", "End", "Score", "Strand", "Frame", "Attributes"]

sxlset= df["Attributes"].str.contains("Sxl")


plt.figure()
plt.title("Sxl Starting Position")
plt.plot(df[sxlset]["Start"])
plt.ylabel("start position")
plt.xlabel("genes")
plt.savefig("SxlStart.png")