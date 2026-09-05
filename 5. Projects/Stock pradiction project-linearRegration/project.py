from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd
import math
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('data.csv')

# Features
x = df[['Open', 'High', 'Low', 'Last',
        'Total Trade Quantity', 'Turnover (Lacs)']]

# Target
y = df[['Close']]

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(x_train, y_train)

# Predict
y_pred = model.predict(x_test)

# Accuracy
mae = round(mean_absolute_error(y_test, y_pred),2)
mse = round(mean_squared_error(y_test, y_pred),2)
rmse = round(math.sqrt(mse),2)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)

plt.plot(y_test.values[:20], label='Actual')
plt.plot(y_pred[:20], label='Predicted')

plt.legend()
plt.show()

# User input
open_price = float(input("Enter Open Price: "))
high_price = float(input("Enter High Price: "))
low_price = float(input("Enter Low Price: "))
last_price = float(input("Enter Last Price: "))
quantity = float(input("Enter Trade Quantity: "))
turnover = float(input("Enter Turnover: "))

# Prediction
prediction = model.predict([[
    open_price,
    high_price,
    low_price,
    last_price,
    quantity,
    turnover
]])

print("Predicted Close Price:", prediction[0][0])




