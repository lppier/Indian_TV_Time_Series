import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import os
import matplotlib


os.chdir('/Users/pierlim/PycharmProjects/Indian_TV_Time_Series')
df = pd.read_csv("./data/ActualRatings_weeklyGRP.csv")
df = df.drop(df.columns[2], axis=1)
split_str = df['GRPRatingsDate'].str.split('(')
df['GRPRatingsDate'] = split_str.str[0]
df['GRPRatingsDate'] = pd.to_datetime(df['GRPRatingsDate'])

df = df.set_index('GRPRatingsDate')
df.plot()
plt.title('Weekly Ratings 2007 - 2009')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
rolling_mean = df.rolling(4).mean()
rolling_std = df.rolling(4).std()
#ori = ax.plot(df, label='Original')
mean = ax.plot(rolling_mean, label='Moving average mean')
#std = ax.plot(rolling_std, label='Moving average standard deviation')
handles, labels = ax.get_legend_handles_labels()
ax.legend(labels, loc='best')
plt.show()
plt.close()

df_expo = df
df_expo['GRP_Expo'] = df_expo['GRP'] ** 0.9
df_expo = df_expo.drop('GRP', axis=1)


fig2 = plt.figure()
ax2 = fig2.add_subplot(1, 1, 1)
rolling_mean = df_expo.rolling(4).mean()
rolling_std = df_expo.rolling(4).std()
#ori = ax.plot(df_expo, label='Original')
mean = ax2.plot(rolling_mean, label='Moving average mean')
#std = ax.plot(rolling_std, label='Moving average standard deviation')
handles, labels = ax2.get_legend_handles_labels()
ax2.legend(labels, loc='best')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import os
import matplotlib
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np
import math
import numpy as np
import statsmodels.api as sm
import itertools
import sys
from pyramid.arima import auto_arima

def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


os.chdir('/Users/pierlim/PycharmProjects/Indian_TV_Time_Series')
df = pd.read_csv("./data/ActualRatings_weeklyGRP.csv")
df = df.drop(df.columns[2], axis=1)
split_str = df['GRPRatingsDate'].str.split('(')
df['GRPRatingsDate'] = split_str.str[0]
df['GRPRatingsDate'] = pd.to_datetime(df['GRPRatingsDate'])

df = df.set_index('GRPRatingsDate')
df.plot(style='.-')
plt.title('Weekly Ratings 2007 - 2009')
plt.show()
df.tail()