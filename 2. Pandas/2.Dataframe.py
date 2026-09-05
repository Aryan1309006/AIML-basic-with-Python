import pandas as pd

data={"name":["Aryan","bob","sam"],
      "age":[20,30,40]}

df=pd.DataFrame(data)
print(df)

df=pd.DataFrame(data,index=["a","b","c"])
print(df)

print(df.loc["a"])
print(df.iloc[1])
#add a new column
df["job"]=[12,13,14,]
print(df)

# add a new row 
newRow=pd.DataFrame([{
    "name":"asd","age":10,"job":15
}],index=[4])
df=pd.concat([df,newRow])
print(df)