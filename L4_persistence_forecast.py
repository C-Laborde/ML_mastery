import pandas as pd
from aux_func.L4_visualization import describe_and_plot
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt


series = pd.read_csv('data/daily-total-female-births-in-cal.csv', header=0,
                     index_col=0, parse_dates=True, squeeze=True)
series.index = pd.to_datetime(series.index)

# describe_and_plot(series)


# persistence model: predict next obs based on just the current observation

def model_persistence(x):
    return x


prediction = series.shift(1)
prediction = prediction.dropna()

plt.figure()
plt.plot(series)
plt.plot(prediction)

prediction = list(prediction.values)
actual = series.values
actual = actual[1:]

error = sqrt(mean_squared_error(actual, prediction))

print(error)
# plt.figure()
# plt.plot(error)

plt.show()
