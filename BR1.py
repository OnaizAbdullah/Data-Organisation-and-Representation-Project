import pandas as pd #Imports module pandas

#BR1
data = pd.read_csv('CleanedData.csv') #Reads the data from the csv
print(data)

data['AGE'] = data['AGE'].replace(['years and over'], None)

data.to_csv('CleanedData2.csv') #Saves cleaned data to a new file



