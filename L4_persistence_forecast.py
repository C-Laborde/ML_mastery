import pandas as pd
from aux_func.L4_visualization import describe_and_plot
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt


def model_persistence(x):
    return x


series = pd.read_csv('data/daily-total-female-births-in-cal.csv', header=0,
                     index_col=0, parse_dates=True, squeeze=True)
series.index = pd.to_datetime(series.index)

# Uncomment this to see how the data looks like
describe_and_plot(series)

# Define the supervised learning algorithm
actual = pd.DataFrame(series.values)
data = pd.concat([actual, actual.shift(-1)], axis=1)
data.columns = ["t", "t+1"]
data.dropna(inplace=True)
print(data.head())

# Train and Test sets
X = data.values
train_size = int(0.66*len(X))
train, test = X[:train_size], X[train_size:]
x_train, y_train = train[:, 0], train[:, 1]
x_test, y_test = test[:, 0], test[:, 1]

# Persistence model: predict next obs based on just the current observation
prediction = x_test

test_error = sqrt(mean_squared_error(y_test, prediction))
print('Test MSE: %.3f' % test_error)

plt.figure()
plt.plot(x_train.tolist() + [None]*len(x_test))
plt.plot([None]*len(x_train) + y_test.tolist())
plt.plot([None]*len(y_train) + prediction.tolist())
plt.legend(["train", "test", "prediction"])
plt.show()
