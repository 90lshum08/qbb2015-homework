#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats as st
import numpy as np

df = pd.read_table("/Users/cmdb/qbb2015/stringtie/SRR072893/t_data.ctab")

fpkm_df = df[df.FPKM !=0]
FPKM = fpkm_df["FPKM"]

  
  
density = st.kde.gaussian_kde(FPKM)

density.covariance_factor = lambda : .25
density._compute_covariance()

xs=np.arange(0,7000,1)
ys=density(xs)

plt.figure()
plt.title("FPKM Density")
plt.plot(xs, ys)
plt.savefig("density.png")







