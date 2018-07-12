import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.Series(data=[4, 5, 6, 7, 8])

plt.hist(df, bins = range(min
                          (df), max(df)+5, 5))
plt.title("Sample Sz Histogram (" + str(np.sum(df)) + " sz from " + str(df.size) + " rats)")
plt.xlabel("# of Seizures")
plt.ylabel("# of Rats")

fig = plt.gcf()

plt.show()