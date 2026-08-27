import pandas as pd

data = {
    "Name": ["  Ali  ", "Sara", "Ahmed", "Ali", "Hina", "Usman"],
    "Age": [20, 22, 19, 20, 24, 26],
    "Salary": [50000, 60000, 45000, 50000, "abc", "70000"],
    "joining_date": [
        "2024-01-15",
        "2023-06-20",
        "2022-09-10",
        "2024-01-15",
        "2024-03-05",
        "2023-11-12"
    ]
}
df = pd.DataFrame(data)

print(df)
                          #


check_duplicates=df.duplicated()    #it checks which rows is duplicATE,AND IT RETURN true or false
print(check_duplicates)

shows_duplicates_rows=df[df.duplicated()]  #it gives the row which is duplicated
print(shows_duplicates_rows)

remove_duplicates=df.drop_duplicates()  #it reoves the duplicates rows
print(remove_duplicates)

                     #convert any text into numbers or Nan.

"""
df["Salary"]=pd.to_numeric(df["Salary"])

#pandas will give error when we reaches to "abc",so we will use errors=coerce here


"""
df["Salary"]=pd.to_numeric(df["Salary"] , errors="coerce")
print(df["Salary"])

                       #to convert string datetime into real datatime
                       #pd.to_datetime(),It is used when a column contains dates stored as text, and we want Pandas to understand them as actual dates.

df["joining_date"]=pd.to_datetime(df["joining_date"])   #It tell pandas Convert this column into actual date/time data.
print(df["joining_date"])



                            #Now the next part is working with dates using .dt
"""
once we have:
            df["joining_date"] = pd.to_datetime(df["joining_date"])
then we can get the year from each date:
            df["year"] = df["joining_date"].dt.year
"""


df["year"] = df["joining_date"].dt.year
#Creates a new column "year" containing the year from the datetime column

print(df["year"])


df["month"] = df["joining_date"].dt.month
#Creates a new column "month" containing the month from the datetime column

print(df["month"])


df["day"] = df["joining_date"].dt.day
#Creates a new column "day" containing the day of the month from the datetime column

print(df["day"])


#Extract the day name from the joining_date column

df["day_name"] = df["joining_date"].dt.day_name()
#Creates a new column "day_name" containing the name of the day

print(df["day_name"])


"""
1. .str.strip()
              It removes extra spaces from the beginning and end of text.
              examle:
              " Ali " → "Ali"
2. .str.lower()
              Converts text to lower case
              "ALI" → "ali"
              "SARA" → "sara"
3. .str.upper()
              Converts text into upper case
              "ali" → "ALI"
              "sara" → "SARA"
"""

df["Name"] = df["Name"].str.strip()   #it removes extra spaces before and end of the text
print(df["Name"])


df["Name"] = df["Name"].str.lower()    #it onvert text into lower case
print(df["Name"])

df["Name"] = df["Name"].str.upper()    #it converts text into upper case
print(df["Name"])

                             #use of str.contains()
text_containing_h=df["Name"].str.contains("H")  #Show only the rows where the Name contains "a".
print(text_containing_h)



                #filtering data with multiple condition using logical operators
filtered = df[(df["Age"] > 20) & (df["Salary"] > 50000)]
          #this mean Show rows where Age is greater than 20 AND Salary is greater than 50,000.
print(filtered)

                               #OR(|)
filtered = df[(df["Age"] > 23) | (df["Salary"] > 55000)]

print(filtered)



                          #isin() function
                          #.isin() is used when you want to check whether values in a column belong to a specific list of values.

get_specific_data=df[df["Name"].isin(["ALI", "SARA"])] 
print(get_specific_data)

                       #cleaning column names.
df.columns = df.columns.str.strip()  #remove extra spaces
df.columns = df.columns.str.lower()   #convert to lower case