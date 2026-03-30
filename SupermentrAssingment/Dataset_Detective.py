import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())
print(df.max())
print(df.isnull().sum())