import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

bicycle = pd.read_csv("day.csv")
print(bicycle.head())
print(bicycle.describe())
bicycle_x = bicycle[[ 'season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered']].values.reshape(-1, 13)
bicycle_x_train = bicycle_x[:-30]
bicycle_x_test = bicycle_x[-30:]
bicycle_y = bicycle['cnt'].values

bicycle_y_train = bicycle_y[:-30]
bicycle_y_test = bicycle_y[-30:]

model = linear_model.LinearRegression()
model.fit(bicycle_x_train, bicycle_y_train)

bicycle_y_predicted = model.predict(bicycle_x_test)

print("Mean Squared Error is:", mean_squared_error(bicycle_y_predicted, bicycle_y_test))

plt.scatter(bicycle_x_test[:, 0], bicycle_y_test, c="blue", label="Actual")
plt.scatter(bicycle_x_test[:, 0], bicycle_y_predicted, c="red", alpha=0.5, label="Predicted")
plt.legend()
plt.show()
