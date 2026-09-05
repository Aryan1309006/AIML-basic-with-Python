from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import pandas as pd

# Load dataset
df = pd.read_csv('House_price.csv')

print(df.head())

# Features
x = df[[
    "Area_sqft",
    "Bedrooms",
    "Bathrooms",
    "Age_of_House",
    "Distance_from_City_km",
    "Parking"
]]

# Target
y = df["Price"]

# Split dataset
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(x_train, y_train)

# Predict test data
y_pred = model.predict(x_test)

# Error checking
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)

# User input
Area_sqft = float(input("Enter Area_sqft: "))
Bedrooms = float(input("Enter Bedrooms: "))
Bathrooms = float(input("Enter Bathrooms: "))
Age_of_House = float(input("Enter Age_of_House: "))
Distance_from_City_km = float(input("Enter Distance_from_City_km: "))
Parking = float(input("Enter Parking spaces: "))

# Predict new house price
new_price = model.predict([[
    Area_sqft,
    Bedrooms,
    Bathrooms,
    Age_of_House,
    Distance_from_City_km,
    Parking
]])

print("Predicted Price:", round(new_price[0],3))