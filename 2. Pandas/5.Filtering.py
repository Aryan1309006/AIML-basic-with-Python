import pandas as pd

df=pd.read_csv("data.csv")

# filtering


# tall_polimon=df[df["HP"]>=200].to_string()
# print(tall_polimon)
ff=df[(df["Type 1"]=="Rock")&(df["Type 2"]=="Flying")]
print(ff)