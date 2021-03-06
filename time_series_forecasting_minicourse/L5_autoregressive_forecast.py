import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
from pandas.plotting import autocorrelation_plot
from pandas.plotting import lag_plot
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.ar_model import AR
from utils.persistence_model import persistence_model


series = pd.read_csv('data/daily-minimum-temperatures.csv', header=0,
                     index_col=0, parse_dates=True)

"""
Autoregression: Is a linear time series model that uses observations from
previous time steps as input to a regression equation to predict the value at
the next time step.
"""
print(series.tail())
series.column = ['Temp']

# Plot time series
plt.figure()
plt.plot(series)
plt.ylabel("Temperature")
plt.xlabel("Date")

# Calculate correlation matrix
df = pd.concat([series.shift(1), series], axis=1)
df.columns = ["t-1", "t+1"]
result = df.corr()
print(result)

# Check autocorrelation
fig, ((ax1, ax2)) = plt.subplots(2, 1)
autocorrelation_plot(series, ax=ax1)
diag = range(int(series.min()), int(series.max()))
lag_plot(series, ax=ax2)
plt.plot(diag, diag, '--k')
fig.subplots_adjust(hspace=0.4)


# ###### Persistence model as baseline ########

# train-test split (train not required in this case but for rutine we keep it)
X = df.values
train, test = X[1:len(X)-7], X[len(X)-7:]
X_train, y_train = train[:, 0], train[:, 1]
X_test, y_test = test[:, 0], test[:, 1]

# walk-forward validation for 7 1-day forecasts
predictions = list()
for x in X_test:
    yhat = persistence_model(x)
    predictions.append(yhat)
test_score = mean_squared_error(y_test, predictions)
print("Test MSE: %.3f" % test_score)

# plot predictions vs expected
fig, ax = plt.subplots(1, 1)
ax.plot(y_test)
ax.plot(predictions, color="green")
ax.legend()


# #####  Autoregression model for 1 7-days forecast ######
# train Autoregression
series = Series.from_csv('data/daily-minimum-temperatures.csv', header=0)
X = series.values
train, test = X[1:len(X)-7], X[len(X)-7:]
model = AR(train)           # this creates the model
model_fit = model.fit()     # this trains the model in the dataset
print("Lag length: %s" % model_fit.k_ar)
print("Coefficients %s" % model_fit.params)   # The fitted parameters

# make predictions
predictions = model_fit.predict(start=len(train), end=len(train)+len(test)-1,
                                dynamic=False)
for i in range(len(predictions)):
    print("predicted=%f, expected=%f" % (predictions[i], test[i]))

error = mean_squared_error(test, predictions)
print("Test MSE: %f" % error)

fix, ax = plt.subplots(1, 1)
ax.plot(test)
ax.plot(predictions, color="green")
plt.show()
