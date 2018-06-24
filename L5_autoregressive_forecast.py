import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.plotting import autocorrelation_plot


def parser(x):
    return datetime.strptime('200'+x, '%Y-%m')


series = pd.read_csv('data/daily-minimum-temperatures.csv', header=0,
                     index_col=0, parse_dates=True)

"""
Autoregression: Is a time series model that uses observations from previous
time steps as input to a regression equation to predict the value at the next
time step.
"""
print(series.tail())
series.column = ['Temp']

print(series.isnull().sum())
plt.plot(series)

# Check autocorrelation
autocorrelation_plot(series)

plt.show()
