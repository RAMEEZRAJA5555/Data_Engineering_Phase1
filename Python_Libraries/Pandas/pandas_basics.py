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

select_colum=df["season"]       #for selecting only one colum
print(select_colum)

select_multiple_col=df[["win_by_runs","win_by_wickets"]]    #for selecting multiples colums
print(select_multiple_col)


#loc is used to select values using labled based.so in our data labled index starting from 0 and so on,we can also specify labled indexing by using index_col=col_name
labled_based_selection1=df.loc[0]  #Give me the row whose index label is 0

abled_based_selection2=df.loc[2]   #Give me the row whose index label is 1.



                       # Because iloc uses position, you don't care what the index label is.
position_based_selection1=df.iloc[4]  #Give me the 5th row by position.

position_based_selection2=df.iloc[2]  #give me 3rd row by position

print(position_based_selection1)


