import pandas as pd #Imports module pandas

#BR1
df = pd.read_csv('rawdata.csv') #Reads the data from the csv
# print("Original Data")
# print(df) #Displays the raw data

#Rows and columns
# print(df.shape) #Displays the shape of the file
# print(f"Amount of columns in Raw Data:{len(df.columns)}") #Displays the amount of columns there is
# print(f"Amount of rows in Raw Data:{len(df)}") #Prints the amount of rows in the file

df = df.drop(columns=['STUB_NAME_NUM','STUB_LABEL_NUM','INDICATOR']) #Removes unecessary columns
# print(df)

df = df.drop_duplicates() #Drops any duplicate rows
# print(df)

df = df.dropna() #Removes any missing/null values
# print(df)

df['ESTIMATE'] = df['ESTIMATE'].replace(['*'], None) #Replaces any asterstrikes with a blank
# print(df)

df['AGE'] = df['AGE'].replace(['years and over'], None) #Removes the words from the ages.
# print(df)

df.to_csv('CleanedData.csv') #Saves cleaned data to a new file


