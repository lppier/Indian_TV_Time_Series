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


def find_more_than_10_percent(data):
    for index, row in data.iterrows():
        percentage_error = (abs(row['Predicted GRP'] - row['Actual GRP']) / row['Actual GRP']) * 100
        if percentage_error > 10.0:
            print("date: {0} error {1}".format(row['GRPRatingsDate'], percentage_error))




os.chdir('/Users/pierlim/PycharmProjects/IndianTV')
df = pd.read_csv("./data/simple_exp_test.csv")
# df_train = df.dropna()
find_more_than_10_percent(df)
df = df.dropna()
mae = mean_absolute_error(df['Actual GRP'], df['Predicted GRP'])
mse = mean_squared_error(df['Actual GRP'], df['Predicted GRP'])
print('Prediction quality: {:.2f} MSE ({:.2f} RMSE),  ({:.2f} MAE)'.format(mse, math.sqrt(mse), mae))
mape = mean_absolute_percentage_error(df['Actual GRP'], df['Predicted GRP'])
print('Prediction quality: {:.2f}% MAPE '.format(mape))
