import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

from os import listdir, walk
from os.path import isfile, join, splitext


path = 'F:/WilcoxData'

walker = walk(path)

allfiles = [f[0] + '/' + f[2][0] for f in walk(path)
            if f[2]
            if 'Seizure' in f[0]
            if splitext(f[0] + '/' + f[2][0])[1] == '.txt']

# print(allfiles)
allsz = {}

for f in allfiles:
    if os.stat(f).st_size > 0:
        dft = pd.read_csv(f,header=None)
    #     print(dft)

        for i in range(dft.__len__()):
            subject = str(dft.iloc[i][1])
            if subject in allsz:
                # add one seizure to correct spot in allsz
                allsz[subject] += 1
            else:
                # create new entry for subject in allsz initialized to 1
                allsz[subject] = 1

print(allsz)

df = pd.Series(allsz,name='Sz Total')
df.to_csv('szbysub.csv')

plt.hist(df, bins = range(min(df), max(df)+5, 5))
plt.title("Wilcox Sz Histogram (" + str(np.sum(df)) + " sz from " + str(df.size) + " rats)")
plt.xlabel("# of Seizures")
plt.ylabel("# of Rats")

fig = plt.gcf()

plt.show()

