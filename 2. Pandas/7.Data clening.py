import pandas as pd

df=pd.read_csv("data.csv")

# data clining
print(df)
df=df.drop(columns=["Legendary"])
print(df)

# df=df.dropna(subset=["Type 2"])
# print(df.to_string())

# df=df.fillna({"Type 2":"None"})       #this is most imp first we do this then try to drop
# print(df.to_string())

# df["Type 1"]=df["Type 1"].replace({"Grass":"GRASS"})
# print(df.to_string())

# df["Name"]=df["Name"].str.lower()
# print(df.to_string())

# df["Legendary"]=df["Legendary"].astype(bool)
# print(df.to_string())

df=df.drop_duplicates()
print(df)