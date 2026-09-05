import pandas as pd

df=pd.read_csv("data.csv")
print(df)

#selection by column

# print(df["Name"])
# print(df["Name"].to_string())     for complete file

# print(df[["Name","Type 1"]])

#select by row

print(df.loc[0])