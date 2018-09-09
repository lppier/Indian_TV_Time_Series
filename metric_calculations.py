import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import math


def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


os.chdir('/Users/pierlim/PycharmProjects/IndianTV')
df = pd.read_csv("./data/arima111_predicted.csv")

mae = mean_absolute_error(df['Actual'], df['Predicted'])
mse = mean_squared_error(df['Actual'], df['Predicted'])
print('Prediction quality: {:.2f} MSE ({:.2f} RMSE),  ({:.2f} MAE)'.format(mse, math.sqrt(mse), mae))
mape = mean_absolute_percentage_error(df['Actual'], df['Predicted'])
print('Prediction quality: {:.2f}% MAPE '.format(mape))
