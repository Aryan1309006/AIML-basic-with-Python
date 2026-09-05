# Import required libraries
from sklearn.model_selection import train_test_split
import pandas as pd

# Create dataset
data = {
    'Studyhr': [1, 2, 3, 4, 5],
    'TestScore': [40, 50, 60, 70, 80]
}

# Create DataFrame
df = pd.DataFrame(data)

# ---------------- Features and Target ----------------
# X = Input data
# Y = Output/Result data

x = df[['Studyhr']]      # Feature column
y = df[['TestScore']]    # Target column

# ---------------- Train-Test Split ----------------
# test_size=0.2 means 20% data for testing
# random_state=42 gives same output every run

x_train, x_test, y_train, y_test = train_test_split(
    x, y,
    test_size=0.2,
    random_state=42
)

# Display training and testing data
print("X Training Data:\n", x_train)

print("\nX Testing Data:\n", x_test)

print("\nY Training Data:\n", y_train)

print("\nY Testing Data:\n", y_test)


# ---------------- Machine Learning Steps ----------------
# 1. Clean Data
# 2. Encode Categorical Data
# 3. Split Data (Train/Test)
# 4. Train Model
# 5. Test Model