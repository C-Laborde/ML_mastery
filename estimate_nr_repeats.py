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

# check if the average stabilizes after 1000 results
partial_avg = [(df.iloc[:i]).mean() for i in range(df.size)]
fig, ax = plt.subplots(1, 1)
ax.plot(partial_avg)
ax.axhline(y=df["results"].mean(), color="r")

# standard_error = sample_standard_deviation / sqrt(number of repeats)
partial_ste = [df.iloc[:i].std()/i**.5 for i in range(1, df.size+1)]
fig, ax = plt.subplots(1, 1)
ax.plot(partial_ste)
# the horizontal lines help to determine what number of experiments are
# required for different standar deviations
ax.axhline(y=0.5, color="r")
ax.axhline(y=1, color="r")

# we calculate the confidence interval for each number of repeats and add it
# as error bars
fig, ax = plt.subplots(1, 1)
conf = [std * 1.96 for std in partial_ste]
plt.errorbar(range(len(partial_avg)), partial_avg, yerr=conf)
ax.axhline(y=df["results"].mean(), color="r")
plt.show()
