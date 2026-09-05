#based on neareestb values predict desision
# eg.email spam or not 
# steps choose k val->closest point->HM in each class 
# tip k=odd 


# Import K-Nearest Neighbors Classifier
from sklearn.neighbors import KNeighborsClassifier

# ---------------- Training Data ----------------
# [Height, Weight]

x = [
    [5.5, 120],
    [5.7, 130],
    [6.0, 150],
    [4.8, 90],
    [5.0, 95],
    [6.2, 160]
]

# Labels
# 0 = Apple
# 1 = Orange

y = [0, 0, 0, 1, 1, 1]

# ---------------- Create Model ----------------
# n_neighbors=3 means check nearest 3 points

model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(x, y)

# ---------------- User Input ----------------
height = float(input("Enter height: "))
weight = float(input("Enter weight: "))

# Predict fruit
prediction = model.predict([[height, weight]])[0]

# [0] is used because predict() returns a list
# Example: [0] or [1]
# We only need the actual value

# ---------------- Output ----------------
if prediction == 0:
    print("Apple")
else:
    print("Orange")


"""
---------------- KNN Algorithm ----------------

KNN = K-Nearest Neighbors

Used for classification problems like:
- Spam or Not Spam
- Apple or Orange
- Pass or Fail

How it works:
1. Choose K value
2. Find nearest points
3. Check majority class
4. Predict result

Tip:
- Use odd K values like 3,5,7
- Helps avoid tie situations

Basic Syntax:

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=3)

model.fit(x, y)

prediction = model.predict([[value]])

"""