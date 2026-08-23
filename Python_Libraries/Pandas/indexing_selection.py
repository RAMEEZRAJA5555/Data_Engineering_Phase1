#indexing selection is done using loc(labled based selection) and iloc(position based selection)


import pandas as pd

df = pd.read_csv("IPL_matches.csv")

#Select one column
select_column = df["season"]

print(select_column)

#Select multiple columns
select_columns = df[["season", "team1", "team2", "winner"]]

print(select_columns)


"""
loc is used for label-based selection.

It selects rows and columns using their labels.
If we specify an index column while loading the data,
that column becomes the DataFrame's index and its values
can be used as row labels with loc.
exampe:
df=pd.read_csv("IPL_mathces.csv, index_col="id")

result=df.loc[3] it will give rows with index label 3

Now the id column becomes the index and can be used
as a label with loc.


"""

# Select one row using its index label
print(df.loc[0])


# Select rows from index label 0 to 4
# loc includes the ending label
print(df.loc[0:4])


# Select a specific value using row label and column label
print(df.loc[0, "season"])


# Select specific rows and columns using their labels
print(df.loc[0:4, ["season", "team1", "team2"]])


"""
iloc is used for position-based selection.

It selects rows and columns according to their numerical
position, starting from 0.
"""

# Select the first row
print(df.iloc[0])


# Select rows from position 0 to 4
# iloc does not include the ending position
print(df.iloc[0:5])


# Select a specific value using row and column positions
print(df.iloc[0, 1])


# Select rows 0 to 4 and columns 1 to 3
print(df.iloc[0:5, 1:4])