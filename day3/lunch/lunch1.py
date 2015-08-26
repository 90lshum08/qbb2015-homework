#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

metadata = pd.read_csv("~/qbb2015/rawdata/samples.csv")
metadata2 = pd.read_csv("~/qbb2015/rawdata/replicates.csv")

Sxlfemale = []
Sxlmale = []
Sxlreplicates = []

for sample in metadata[metadata["sex"] == "female"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    Sxlfemale.append(df[roi]["FPKM"].values)
    
for sample in metadata[metadata["sex"] == "male"]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    Sxlmale.append(df[roi]["FPKM"].values)

for sample in metadata2[metadata2["stage"].str.contains("14")]["sample"]:
    df = pd.read_table("~/qbb2015/stringtie/" + sample + "/t_data.ctab")
    roi = df["t_name"].str.contains("FBtr0331261")
    Sxlreplicates.append(df[roi]["FPKM"].values)
   
plt.figure()
plt.title("FPKM Timecourse")
plt.plot(Sxlfemale, "b", label = "Female")
plt.plot(Sxlmale, "r", label = "Male")
plt.plot(range(len(Sxlreplicates)),Sxlreplicates,'o', color = "g", label = "Replicates")
plt.legend(loc="upper left")
plt.xlabel("Developmental Stage")
plt.ylabel("Abundance (FPKM)")
plt.xticks(range(len(Sxlfemale)), metadata["stage"])
plt.savefig("timecourseMFR.png")