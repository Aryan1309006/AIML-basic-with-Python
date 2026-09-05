import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import median_absolute_error,mean_squared_error,r2_score
# import matplotlib.pyplot as plt

data=pd.read_csv('project2.csv')

x=data[["Study_Hours_Per_Week"]]
y=data[["Monthly_Test_Score"]]

model=LinearRegression()
model.fit(x,y)

Predicted_result=model.predict(x)

# validregratin matrix
mae=mean_squared_error(y,Predicted_result)
mse=mean_squared_error(y,Predicted_result)
rmse=np.sqrt(mse)
r2=r2_score(y,Predicted_result)

print("Result:")
print("MAE:",round(mae,2))
print("MSE:",round(mse,2))
print("RMSE:",round(rmse,2))
print("r*2:",round(r2,2))