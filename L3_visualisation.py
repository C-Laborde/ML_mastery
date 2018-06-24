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


# ### Inspect the data and print some basic information
print("#### Sales of shampoo ####\n")

series_shampoo = pd.read_csv('data/sales-of-shampoo-over-a-three-ye.csv',
                             header=0, index_col=0, parse_dates=[0], nrows=36,
                             squeeze=True, date_parser=parser)
print(series_shampoo.head(10))
print("\n")
print('Size = %d \n' % series_shampoo.size)
print("\n")
print("Stats:")
print(series_shampoo.describe())
print("Nr of NaNs = %d" % series_shampoo.isnull().sum())

# ### Time series plots

# We group the data per year
series_shampoo_groups = series_shampoo.groupby(TimeGrouper('A'))
years = pd.DataFrame()
for name, group in series_shampoo_groups:
    years[name.year] = group.values

years.columns = ["2001", "2002", "2003"]

# Prepare the figure where the plots will be placed
fig, ((ax1, ax2), (ax3, ax4),
      (ax5, ax6), (ax7, ax8)) = plt.subplots(4, 2, sharex=False, sharey=False,
                                             figsize=(16, 28))

# Line plots
ax1.plot(series_shampoo)
ax1.set(xlabel="Date", ylabel="Sales", title="Line plot")

ax2.plot(years)
ax2.set(xlabel="Month", ylabel="Sales", title="Line plot per year")
ax2.legend(["2001", "2002", "2003"], loc="upper left")


# Histograms and density plot
# ax3.hist(series_shampoo, bins=20)
sns.distplot(series_shampoo, rug=True, bins=20, ax=ax3)
ax3.set(xlabel="Sales", ylabel="Counts", title="Histogram and density plot")
# series_shampoo.plot(kind="kde")

# Box and whisker plot
# ax4.boxplot(years, column=["2001", "2002", "2003"])
years.boxplot(column=["2001", "2002", "2003"], ax=ax4)
ax4.set(xlabel="Years", ylabel="Sales", title="Box and whisker plot")

# Heatmap plot
img5 = ax5.matshow(years, interpolation=None, aspect='auto')
xaxis = [2000, 2001, 2002, 2003]
yaxis = range(-1, 13, 2)
ax5.set(xlabel="Year", ylabel="Month", xticklabels=xaxis, yticklabels=yaxis,
        title="Heatmap plot")
ax5.xaxis.tick_bottom()
fig.colorbar(img5, ax=ax5, aspect=5)

# Lag plot
lag_plot(series_shampoo, ax=ax6)
diagonal = range(int(series_shampoo.min()), int(series_shampoo.max()))
ax6.plot(diagonal, diagonal, '--k')
ax6.set(xlabel="Sales(t)", ylabel="Sales(t+1)", title="Lag plot")

# Autocorrelation plot
autocorrelation_plot(series_shampoo, ax=ax7)
ax7.set(title="Autocorrelation plot", ylim=(-1, 1))

ax8.remove()

fig.subplots_adjust(hspace=0.6)
# plt.tight_layout()
plt.show()
