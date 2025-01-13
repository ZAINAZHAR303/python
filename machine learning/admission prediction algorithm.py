import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
data = pd.read_csv("Admission_Predict.csv")
print(data.columns)
#print(data.head())
#print(data.keys())
'''['Serial No.', 'GRE Score', 'TOEFL Score', 'University Rating', 'SOP',
       'LOR ', 'CGPA', 'Research', 'Chance of Admit '],
      dtype='object')'''

x = data[['Serial No.', 'GRE Score', 'TOEFL Score', 'University Rating', 'SOP',
       'LOR ', 'CGPA', 'Research']]
y = data['Chance of Admit ']


x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.1, random_state=42)

model= LinearRegression()
model.fit(x_train,y_train)

prediction_y= model.predict(x_test)

df= pd.DataFrame({"Actual":y_test, "prediction":prediction_y})
print(df)

print(len(x_test), len(prediction_y))

plt.scatter(y_test,prediction_y)
#plt.scatter(x_test,y_test)

plt.show()


print("the mean square error  of model is:", mean_squared_error(y_test,prediction_y))
print("the mean absolute error  of model is:", mean_absolute_error(y_test,prediction_y))