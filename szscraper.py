import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

from os import listdir, walk
from os.path import isfile, join, splitext


path = 'F:/WilcoxData/'

walker = walk(path)

allfiles = [f[0] + '/' + f[2][0] for f in walk(path)
            if f[2]
            if 'Seizure' in f[0]
            if splitext(f[0] + '/' + f[2][0])[1] == '.txt']

print(allfiles)
print(len(allfiles))

allsz = pd.DataFrame()

for f in allfiles:
    if os.stat(f).st_size > 0:
        dft = pd.read_csv(f,header=None)
        print(dft)
        allsz = pd.concat([allsz,dft])
        #allsz.append(dft,ignore_index=True)

print(allsz)

allsz.to_csv('allsz.csv')