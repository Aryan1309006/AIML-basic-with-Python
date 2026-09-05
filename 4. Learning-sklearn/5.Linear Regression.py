# Import Linear Regression model
from sklearn.linear_model import LinearRegression

# Input data (Study Hours)
x = [[1], [2], [3], [4], [5]]

# Output data (Marks)
y = [[40], [50], [65], [80], [90]]

# Create Linear Regression model
model = LinearRegression()

# Train the model using x and y data
model.fit(x, y)

# Take user input
hours = float(input("How many hours did you study? "))

# Predict marks based on study hours
predicted_marks = model.predict([[hours]])

# Display prediction
print(f"Based on {hours} hours of study, you may score {predicted_marks[0][0]:.2f} marks")


"""
---------------- Linear Regression ----------------

Used to predict continuous numeric values.

Basic Syntax:

from sklearn.linear_model import LinearRegression

# Create model
model = LinearRegression()

# Train model
model.fit(x, y)

# Predict output
prediction = model.predict([[value]])

"""