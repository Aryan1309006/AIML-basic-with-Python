# Import evaluation metrics
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# ---------------- Actual Values ----------------
# True/Correct answers

y_true = [1, 0, 1, 1, 0, 1, 0]

# ---------------- Predicted Values ----------------
# Model predictions

y_pred = [1, 0, 1, 0, 0, 1, 1]

# ---------------- Accuracy ----------------
# Accuracy = Correct Predictions / Total Predictions

print("Accuracy:", accuracy_score(y_true, y_pred))

# ---------------- Precision ----------------
# Precision = Correct Positive Predictions / Total Positive Predicted

print("Precision:", precision_score(y_true, y_pred))

# ---------------- Recall ----------------
# Recall = Correct Positive Predictions / Actual Positives

print("Recall:", recall_score(y_true, y_pred))

# ---------------- F1 Score ----------------
# F1 Score = Balance between Precision and Recall

print("F1 Score:", f1_score(y_true, y_pred))


"""
---------------- Model Evaluation Metrics ----------------

1. Accuracy
   - Overall correctness of model

2. Precision
   - How many predicted positives are correct

3. Recall
   - How many actual positives are found

4. F1 Score
   - Harmonic mean of Precision and Recall

Basic Syntax:

from sklearn.metrics import accuracy_score

accuracy_score(y_true, y_pred)

"""