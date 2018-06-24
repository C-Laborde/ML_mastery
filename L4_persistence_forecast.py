import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from pandas import TimeGrouper
from pandas.plotting import lag_plot
from pandas.plotting import autocorrelation_plot


def parser(x):
    return datetime.strptime('200'+x, '%Y-%m')


series = pd.read_csv('data/daily-total-female-births-in-cal.csv', header=0,
                     index_col=0, parse_dates=True, squeeze=True)
series.index = pd.to_datetime(series.index)

# ### Inspect the data and print some basic information
print("\n")
print("#### Daily total female births ####\n")
print(series.head())
print("\n")
print('Size = %d \n' % series.size)

interest_date = "1959-06-21"
print("Nr of births on %s = %d \n" % (interest_date, series[interest_date]))

print("Stats:")
print(series.describe())
print("-" * 50)

print("\n")


# ### Time series plots

# We group the data per month
series_groups = series.groupby(TimeGrouper('M'))
months = pd.DataFrame()
for name, group in series_groups:
    # pd.Series to fix difference in columns length
    months[name.month] = pd.Series(group.values)

# years.columns = ["2001", "2002", "2003"]

# Prepare the figure where the plots will be placed
fig, ((ax1, ax2), (ax3, ax4),
      (ax5, ax6)) = plt.subplots(3, 2, sharex=False, sharey=False,
                                             figsize=(16, 28))

# Line plots
ax1.plot(series)
ax1.set(xlabel="Date", ylabel="Daily Births", title="Line plot")

# Histograms and density plot
# ax2.hist(series_shampoo, bins=20)
sns.distplot(series, rug=True, bins=20, ax=ax2)
ax2.set(xlabel="Sales", ylabel="Counts", title="Histogram and density plot")

# Box and whisker plot
months.boxplot(ax=ax3)
ax3.set(xlabel="Months", ylabel="Daily Births", title="Box and whisker plot")

# Heatmap plot
img4 = ax4.matshow(months, interpolation=None, aspect='auto')
xaxis = range(-1, 13, 2)
yaxis = range(-4, 33, 5)
ax4.set(xlabel="Month", ylabel="Day", xticklabels=xaxis, yticklabels=yaxis,
        title="Heatmap plot")
ax4.xaxis.tick_bottom()
fig.colorbar(img4, ax=ax4, aspect=5)

# Lag plot
lag_plot(series, ax=ax5)
diagonal = range(int(series.min()), int(series.max()))
ax5.plot(diagonal, diagonal, '--k')
ax5.set(xlabel="Births(t)", ylabel="Births(t+1)", title="Lag plot")

# Autocorrelation plot
autocorrelation_plot(series, ax=ax6)
ax6.set(title="Autocorrelation plot", ylim=(-1, 1))

fig.subplots_adjust(hspace=0.6)
# plt.tight_layout()
plt.show()
