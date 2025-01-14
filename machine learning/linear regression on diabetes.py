import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

#['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

diabetes = datasets.load_diabetes()
print(diabetes.keys())
diabetes_x = diabetes.data
print(pd.keys(diabetes_x))
diabetes_x_train = diabetes_x[:-30]
diabetes_x_test = diabetes_x[-30:]



diabetes_y_train = diabetes.target[:-30]
diabetes_y_test = diabetes.target[-30:]

model = linear_model.LinearRegression()
model.fit(diabetes_x_train,diabetes_y_train)

diabetes_y_predicted= model.predict(diabetes_x_test)
mse= mean_squared_error(diabetes_y_test,diabetes_y_predicted)
rsme = np.sqrt(mse)
print(" root mean squared error is:", rsme)
weight= model.coef_
print("weight",weight)
print("intercept",model.intercept_)


plt.scatter(diabetes_x_test[:,0],diabetes_y_test, c="red")
plt.scatter(diabetes_x_test[:,0],diabetes_y_predicted , c="blue")
plt.show()




