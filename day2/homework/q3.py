#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

annotation = "/Users/cmdb/qbb2015/rawdata/samples.csv"
f= open(annotation)

df = pd.read_table(f, sep=",")
sample_names=df["sample"]

for sample in sample_names:
    sample_table="/Users/cmdb/qbb2015/stringtie/%s/t_data.ctab" % (str(sample))
    file = open(sample_table)
    sample_df = pd.read_table (file)
    
    transcript=sample_df["t_name"].str.contains("FBtr0331261")
    
    print sample_df[transcript]


