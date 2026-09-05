# Import Logistic Regression model
from sklearn.linear_model import LogisticRegression

# Input data (Study Hours)
x = [[1], [2], [3], [4], [5]]

# Output data
# 0 = Fail
# 1 = Pass
y = [0, 0, 1, 1, 1]

# Create Logistic Regression model
model = LogisticRegression()

# Train the model
model.fit(x, y)

# Take user input
hours = float(input("Enter study hours: "))

# Predict result
result = model.predict([[hours]])[0]

# Display output
if result == 0:
    print("Fail")
else:
    print("Pass")


"""
---------------- Logistic Regression ----------------

Used for classification problems.
It predicts categories like:
- Yes / No
- Pass / Fail
- True / False

Basic Syntax:

from sklearn.linear_model import LogisticRegression

# Create model
model = LogisticRegression()

# Train model
model.fit(x, y)

# Predict class
result = model.predict([[value]])

"""