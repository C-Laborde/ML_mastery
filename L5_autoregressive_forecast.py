import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from pandas.plotting import autocorrelation_plot
from pandas.plotting import lag_plot


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

plt.figure()
plt.plot(series)
plt.ylabel("Temperature")
plt.xlabel("Year")

# Check autocorrelation
fig, ((ax1, ax2)) = plt.subplots(2, 1)
autocorrelation_plot(series, ax=ax1)
diag = range(int(series.min()), int(series.max()))
lag_plot(series, ax=ax2)
plt.plot(diag, diag, '--k')

fig.subplots_adjust(hspace=0.4)

plt.show()
