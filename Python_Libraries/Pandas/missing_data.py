

import pandas as pd

df=pd.read_csv("student.csv")

print(df)

#isnull() checks every cell for missing values (True = missing, False = not missing)
print(df.isnull())  

print(df.isna())    # isna() does the same thing as isnull() — checks for missing values


#isnull().sum() counts the number of missing values in each column
print(df.isnull().sum())

# df[df.isna().any(axis=1)] selects rows that contain at least one missing value

missing_val_in_rows=df[df.isnull().any(axis=1)]  #it shows the rows which have the missing values,it display only rows which have missing values

print(missing_val_in_rows)

# dropna() removes rows that contain missing values

drop_missing_val=df.dropna()
print(drop_missing_val)


# fillna() replaces missing values with a specified value
fill_missing=df.fillna("unknown")
print(fill_missing)

# fillna("Unknown") replaces missing values in the City column with "Unknown"

fill_val_in_col=df["Age"].fillna(22)
print(fill_val_in_col)

"""
fill_median_of_col=df["Salary"].fillna(df["Salary"].median())
print(fill_median_of_col)

here we can take meidan of salary bcuz salray col has string values not numeric first convert into numeric values


"""
# pd.to_numeric() converts values into numeric values
#(errors=coerce) If a value cannot be converted to a number, don't give me an error; turn that value into NaN."
#if colum contain "abc" value and this value cannot be converted into number so pandas just write replaces Nan on "abc"
#if value is 50000 --> 50000 will be converted into number sccessfully bcuz its already a number
#if value contain commas, like 50,000 so they aren't directly recognized as plain numbers and become NaN.

df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce") # errors="coerce" changes values that cannot be converted into numbers to NaN
print(df["Salary"])

# fillna(df["Salary"].median()) replaces missing Salary values with the median Salary
fill_median_of_col=df["Salary"].fillna(df["Salary"].median())
print(fill_median_of_col)









