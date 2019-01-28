import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.parser import parser
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error


df = pd.read_csv("data/sales-of-shampoo-over-a-three-ye.csv", header=0,
                 index_col=0, parse_dates=True, date_parser=parser,
                 names=["sales"])

X = df["sales"].values
train_len = int(len(X) * 0.66)

train, test = X[:train_len], X[train_len:]

# new obsevations are appended to history for the rolling forecasting
history = np.copy(train).tolist()
predictions = []
p = 5
d = 1
q = 0

for t in range(len(test)):
    model = ARIMA(history, order=(p, d, q))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0][0]
    predictions.append(yhat)
    real_obs = test[t]
    history.append(real_obs)

errors = test - predictions
print(errors)
error = mean_squared_error(test, predictions)
plt.hist(errors)

plt.figure()
plt.plot(test, color="g")
plt.plot(predictions, color="r")
plt.show()
