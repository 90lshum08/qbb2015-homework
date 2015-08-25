#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header = None)
df.columns = ["Chromosome", "Database", "Type", "Start", "End", "Score", "Strand", "Frame", "Attributes"]

sxlset= df["Attributes"].str.contains("Sxl")
df2=df[sxlset]
sxltrans=df2["Type"].str.contains("transcript")

plt.figure()
plt.title("Sxl Transcript Starting Position")
plt.plot(df2[sxltrans]["Start"])
plt.ylabel("start position")
plt.xlabel("genes")
plt.savefig("SxlTranscript.png")