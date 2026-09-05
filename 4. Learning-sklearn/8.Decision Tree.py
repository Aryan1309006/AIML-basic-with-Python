# Import Decision Tree Classifier
from sklearn.tree import DecisionTreeClassifier

# ---------------- Training Data ----------------
# [Size, Shade]

x = [
    [7, 5],
    [8, 6],
    [9, 6],
    [10, 4],
    [6, 4],
    [5, 5]
]

# Labels
# 0 = Apple
# 1 = Orange

y = [1, 1, 1, 1, 0, 0]

# ---------------- Create Model ----------------
model = DecisionTreeClassifier()

# Train the model
# Decision Tree learns patterns from data
model.fit(x, y)

# ---------------- User Input ----------------
size = float(input("Enter size: "))
shade = float(input("Enter shade: "))

# Predict result
result = model.predict([[size, shade]])[0]

# predict() returns a list like [0] or [1]
# [0] extracts the actual value

# ---------------- Output ----------------
if result == 0:
    print("Apple")
else:
    print("Orange")


"""
---------------- Decision Tree ----------------

Used for classification and prediction.

Works like a flowchart:
- Checks conditions
- Splits data into branches
- Makes decisions step-by-step

Examples:
- Spam Detection
- Fruit Classification
- Disease Prediction

Basic Syntax:

from sklearn.tree import DecisionTreeClassifier

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(x, y)

# Predict output
result = model.predict([[value]])

"""