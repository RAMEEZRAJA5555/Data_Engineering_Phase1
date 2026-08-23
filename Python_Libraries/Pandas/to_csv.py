import pandas as pd

data={
    "name":["ali","salman","akash","abubaker"],
    "age":[20,34,12,34],
    "adress":["multan","lahore","karachi","murree"],
    "marks":[56,78,98,67]
}

df=pd.DataFrame(data)     #dataset for the marks
print(df)


raw_into_csv=df.to_csv("marks.csv", index=False)  #it converts raw data into csv file 

print(df.head(2))    #give me first 2 rows of the dataframe