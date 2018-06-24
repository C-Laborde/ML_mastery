import pandas as pd
from aux_func.L4_visualization import describe_and_plot


series = pd.read_csv('data/daily-total-female-births-in-cal.csv', header=0,
                     index_col=0, parse_dates=True, squeeze=True)
series.index = pd.to_datetime(series.index)

describe_and_plot(series)
