# ---------------- Import Libraries ----------------

import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


# ---------------- Create Dataset ----------------

data = {
    'StudyHours': [1, 2, 3, 4, 5, 6, 7],
    'Gender': ['M', 'F', 'M', 'F', 'M', 'F', 'M'],
    'Result': ['Fail', 'Fail', 'Fail', 'Pass', 'Pass', 'Pass', 'Pass']
}

df = pd.DataFrame(data)

print("Original Data:\n")
print(df)


# ---------------- Encoding ----------------
# Convert text into numbers

le = LabelEncoder()

df['Gender'] = le.fit_transform(df['Gender'])
df['Result'] = le.fit_transform(df['Result'])

print("\nEncoded Data:\n")
print(df)


# ---------------- Features and Target ----------------

x = df[['StudyHours', 'Gender']]
y = df['Result']


# ---------------- Train Test Split ----------------

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=42
)


# ---------------- Train Model ----------------

model = LogisticRegression()

model.fit(x_train, y_train)


# ---------------- Prediction ----------------

prediction = model.predict(x_test)

print("\nPredictions:", prediction)


# ---------------- Evaluation ----------------

print("\nAccuracy:", accuracy_score(y_test, prediction))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, prediction))