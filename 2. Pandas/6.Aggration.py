import pandas as pd

df=pd.read_csv("data.csv")

print("Mean values:\n")
print(df.mean(numeric_only=True))
print("\nSum:\n")
print(df.sum(numeric_only=True))
print("\nMinimum values:\n")
print(df.min(numeric_only=True))
print("\nMaximum values:\n")
print(df.max(numeric_only=True))

print("\nGrouped by Type 1\n")
group= df.groupby("Type 1")
print(group)