# Import required libraries
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd

# Create dataset
data = {
    'Studyhr': [1, 2, 3, 4, 5],
    'TestScore': [40, 50, 60, 70, 80]
}

# Create DataFrame
df = pd.DataFrame(data)

# ---------------- Standard Scaling ----------------
# Formula: Z = (x - mean) / standard deviation

standard_scaler = StandardScaler()

# Apply Standard Scaling
standard_scaled = standard_scaler.fit_transform(df)

# Display scaled data
print("Standard Scaler Output:\n")
print(pd.DataFrame(standard_scaled))


# ---------------- Min-Max Scaling ----------------
# Formula: (x - xmin) / (xmax - xmin)

minmax_scaler = MinMaxScaler()

# Apply Min-Max Scaling
minmax_scaled = minmax_scaler.fit_transform(df)

# Display scaled data
print("\nMin-Max Scaler Output:\n")
print(pd.DataFrame(minmax_scaled))