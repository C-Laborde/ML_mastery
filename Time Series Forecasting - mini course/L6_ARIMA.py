import pandas as pd
from utils.parser import parser
from pandas.plotting import autocorrelation_plot
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from pandas import DataFrame


df = pd.read_csv("data/sales-of-shampoo-over-a-three-ye.csv", header=0,
                 index_col=0, parse_dates=True, date_parser=parser,
                 squeeze=True)

# autocorr shows significant positive correlation with the ~first 5 gaps then
# a good starting point for the AR parameter can be p = 5
autocorrelation_plot(df)

# ###### ARIMA model #####
# The dataset has a clear trend so the time series is not stationary and
# requires differencing to make it stationary, at least a difference order p=1.
p = 5
d = 1
q = 0
model = ARIMA(df, order=(p, d, q))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# residual errors plots suggest that there may still be some trend information
# not captured by the model.
fig, ax = plt.subplots(1, 1)
residuals = model_fit.resid
plt.plot(residuals)

residuals = DataFrame(residuals)
residuals.plot(kind="kde")
plt.show()
