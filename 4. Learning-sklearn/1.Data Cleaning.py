# Import pandas library
import pandas as pd

# Create dataset with missing values
data = {
    'name': ['aryan', 'kapil', 'lalit', 'ram', 'om'],
    'age': [19, None, 20, None, 25],
    'salary': [50000, 60000, 700000, None, None]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print original DataFrame
print("Original DataFrame:")
print(df)

# Show percentage of missing values
print("\nPercentage of Missing Values:")
print(df.isnull().mean() * 100)

# Count total missing values
print("\nCount of Missing Values:")
print(df.isnull().sum())

# Drop rows containing missing values
df_drop = df.dropna()

print("\nDataFrame after dropping missing values:")
print(df_drop)

# Fill missing age values with mean age
df['age'].fillna(df['age'].mean(), inplace=True)

# Fill missing salary values with mean salary
df['salary'].fillna(df['salary'].mean(), inplace=True)

# Print updated DataFrame
print("\nDataFrame after filling missing values:")
print(df)