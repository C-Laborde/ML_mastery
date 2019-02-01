from numpy.random import seed
from numpy.random import normal
from numpy import savetxt
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# let's simulate the result of 1000 trainings of known distribution
mean = 60
sd = 10

seed(1)
results = normal(mean, sd, 1000)
# savetxt("data/sim_results.csv", results)


# statistical analysis on the data
df = pd.read_csv("data/sim_results.csv", header=None)
df.rename(columns={0: "results"}, inplace=True)
# basic stats
print(df.describe())
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.boxplot(df.iloc[:, 0])
ax2.hist(df["results"])

print(df.iloc[:5].mean())
# check if the average stabilizes after 1000 results
partial_avg = [(df.iloc[:i]).mean() for i in range(df.size)]
fig, ax = plt.subplots(1, 1)
ax.plot(partial_avg)


plt.show()
