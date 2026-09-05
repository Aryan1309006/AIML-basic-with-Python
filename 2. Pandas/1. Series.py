import pandas as pd

print("version of pandas:",pd.__version__)


# 1series 

# data=[100.1,102.2,104.3]
# series=pd.Series(data)
# print(series)


data=[100,102,104]
series=pd.Series(data,index=["a","b","c"])
print(series)

print("loc:",series.loc["a"])

series.loc["a"]=200
print(series)

print("iloc:",series.iloc[2])


data=[100,102,104,200,300,400]
series=pd.Series(data,index=["a","b","c","d","e","f"])

print(series[series>=200])
print(series[series<200])



calories={
    "Day1":1750,
    "Day2":2200,
    "Day3":1007,
}
series=pd.Series(calories)
print(series)
print(series.loc["Day1"])

print(series[series>=2000])


