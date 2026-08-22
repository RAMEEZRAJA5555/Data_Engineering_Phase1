import pandas as pd

df=pd.read_csv("IPL_matches.csv")


print(df.head())    #it gives the first 5 rows of datasets

print(df.head(4))   #it gives the first 4 rows

print(df.tail())    #it gives the last 5 rows

print(df.tail(6))   #it gives the last 6 rows of datase

print(df.info())    #gives information about columns, data types,
                    #non-null values, and memory usage


print(df.describe())  #it describe only statistical information about numeric.
                      ## columns (count, mean, std, min, max, etc.)


shap=df.shape      #shape of dataset (636,18)
print(shap)

col=df.columns           #to see the colums of datasets
print(col)

datatypes=df.dtypes       #to check tha datatype o colums
print(datatypes)