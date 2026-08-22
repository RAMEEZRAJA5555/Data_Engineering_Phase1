#how to select colums of the datasets

import pandas as pd

df=pd.read_csv("IPL_matches.csv")  #load data

season_col=df["season"]     #select single column
print(season_col)

multiple_col=df[["season","team1"]]  #select multiple columns
print(multiple_col)         