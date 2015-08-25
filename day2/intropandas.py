#!/usr/bin/env python

import pandas as pd

annotation = "/Users/cmdb/qbb2015/genomes/BDGP6.Ensembl.81.gtf"

df = pd.read_table(annotation, comment='#', header = None)


#print df
#print df.head()
#print df.describe()
#print df.info()

#print df[1:5]
#print df[0:5]
#We want to print lines 10 through 15 (1-based, inclusive)
#print df [9:15]

df.columns = ["Chromosome", "Database", "Type", "Start", "End", "Score", "Strand", "Frame", "Attributes"]

#print df.sort("Type")

#print df["Chromosome"]
#Subset the Chromosome, Start, and End columns
#print df[["Chromosome", "Start", "End"]]

#Subset by row and column
#print df["Start"][9:15]

#print df.shape
df2 = df["Start"]
#print df2.shape

#Save to file with tabs, no column numbers
#df2.to_csv("StartColumn.txt", sep='\t', index=False)

#Find features that start value is less than 10. TO print false: df[~roi]

roi = df["Start"] < 10
print df[roi]

