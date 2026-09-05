import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import median_absolute_error,mean_squared_error

df=pd.read_csv("prioject.csv")
x=df[['Study_Hours']]
y=df[['Marks']]

model=LinearRegression()

model.fit(x,y)

# hours=float(input("Enter houres of study:"))
Predicted_result=model.predict(x)

mae=mean_squared_error(y,Predicted_result)
mse=mean_squared_error(y,Predicted_result)
rmse=np.sqrt(mse)


print("Result:")
print("MAE:",mae)
print("MSE:",mse)
print("RMSE:",rmse)


new_hrs=float(input("Enter hrs of study:"))
new_prediction=model.predict([[new_hrs]])

print("marks will be:",new_prediction)

