import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from pandas import TimeGrouper
from pandas.plotting import lag_plot


def parser(x):
    return datetime.strptime('200'+x, '%Y-%m')


series = pd.read_csv('data/daily-total-female-births-in-cal.csv', header=0,
                     index_col=0, parse_dates=True, squeeze=True)

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
print("#### Sales of shampoo ####\n")

series_shampoo = pd.read_csv('data/sales-of-shampoo-over-a-three-ye.csv',
                             header=0, index_col=0, parse_dates=[0], nrows=36,
                             squeeze=True, date_parser=parser)
print(series_shampoo.head(10))
print("\n")
print("Stats:")
print(series_shampoo.describe())
print("Nr of NaNs = %d" % series_shampoo.isnull().sum())

series_shampoo_groups = series_shampoo.groupby(TimeGrouper('A'))
years = pd.DataFrame()
for name, group in series_shampoo_groups:
    years[name.year] = group.values
# plt.plot(series_shampoo)
# plt.hist(series_shampoo)
# sns.distplot(series_shampoo)
# years.boxplot()
# plt.matshow(years)
lag_plot(series_shampoo)
plt.show()
