import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.Series(data=[4, 5, 6, 9, 56, 45, 68, 28, 85, 143, 240, 280])

plt.hist(df, bins = range(min
                          (df), max(df)+5, 5))
plt.title("Cash Sz Histogram (" + str(np.sum(df)) + " sz from " + str(df.size) + " rats)")
plt.xlabel("# of Seizures")
plt.ylabel("# of Rats")

fig = plt.gcf()

plt.show()