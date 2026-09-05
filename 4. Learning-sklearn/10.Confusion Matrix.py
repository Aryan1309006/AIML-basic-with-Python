# Import confusion matrix
from sklearn.metrics import confusion_matrix

# ---------------- Actual Values ----------------
y_true = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]

# ---------------- Predicted Values ----------------
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 1]

# Create Confusion Matrix
cm = confusion_matrix(y_true, y_pred)

# Display matrix
print("Confusion Matrix:\n", cm)


"""
---------------- Confusion Matrix ----------------

Used to evaluate classification models.

Matrix Format:

        Predicted
          0    1

Actual 0 [TN   FP]
Actual 1 [FN   TP]

Where:

TN = True Negative
     Correctly predicted negative

FP = False Positive
     Wrongly predicted positive

FN = False Negative
     Wrongly predicted negative

TP = True Positive
     Correctly predicted positive


Output:

[[3 2]
 [1 4]]

Meaning:
TN = 3
FP = 2
FN = 1
TP = 4

"""