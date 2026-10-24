#BR2
import pandas as pd #Imports the module pandas
import plotly.express as px #Imports the module plotly as px
from flask import Flask,render_template #Imports python flask and a render_template

df = pd.read_csv('CleanedData.csv') #Reads the cleaned csv data

numeric_columns = ['YEAR_NUM','ESTIMATE'] #Gets a list of strings to convert to numbers and sets it to a variable
for col in numeric_columns: #For every item in the number_columns
    df[col] = pd.to_numeric(df[col], errors = 'coerce') #Converts the values from string to integer

cleaned_file_path = 'CleanedData.csv' #Puts the file path to a variable
df.to_csv(cleaned_file_path, index = False) #Saves the file with the integer values

ignore_column = ['YEAR','STUB_LABEL','PANEL','UNIT','STUB_NAME','AGE'] #Assigns the column 'YEAR' in my dataset to a variable
dictionary = {} #Creates a dictionary

for col in df.columns: #Goes through the columns
    stats_df = df[col] #Used to analyse the dataframe
    if col not in ignore_column: #If the value of col is not in the list of ignored columns
        dictionary[col] = {
            'Mean': stats_df.mean(), #Gets the mean value of the column
            'Median': stats_df.median(), #Gets the median value of the column
            'Mode': stats_df.mode(), #Gets the modal value  of the column
            'Range': stats_df.max() - stats_df.min() #Gets the range of the column
        }
print(dictionary) #Displays the dictionary


#Clean version of the mean,median,mode
stats_df = pd.DataFrame(dictionary).transpose() #Turns the value into a small dataframe
print(stats_df) #Displays the dataframe

#AR3
mean_value = stats_df.loc["ESTIMATE","Mean"] #Gets the mean value of the dictionary
print(f"The mean value for the BMI (ESTIMATE) column is {round(mean_value)}") #Displays the mean value
#Makes suggestions based of the mean BMI value
if mean_value > 24: #If the BMI average is greater than 24
    #print("The average BMI value is very high. I would recommend the government to install more gyms or excerise centres in the country")
    suggestions = (f"The average BMI value for the dataset, {round(mean_value)}, is very high. This is higher than the average BMI of 24 (accroding to the BetterHealth website). I recommend the government to install more gyms or excerise centres in the country") #Makes a suggestion
elif mean_value < 24 and mean_value > 18: #If the mean value is between 18 and 24
    #print("That is a good value for the BMI rate. I recommend to keep up the good work!")
    suggestions = (f"{round(mean_value)} is a good value for the BMI rate according to BetterHealth website. I would recommend to keep up the good work!") #Makes a suggestion
else: #If the mean value is less than 18
    #print("That is a low average. I would recommend to increase the BMI rates/values")
    suggestions = ("f{round(mean_value)} is a low average for BMI value according to BetterHealth. I would recommend to increase the BMI rates/values") #Makes a suggestion
print(f"I say {suggestions}") #Displays the recommended suggestion

SE_value = stats_df.loc["SE (self esteem)","Range"] #Gets the range of the Self-Esteem values in the column
print(f"The range for the Self-Esteem (SE) column is {round(SE_value)}") #Displays the range value
if SE_value > 10: #If the range value is grater than 10
    #print("The Self-Esteem range is very good. I  recommend to keep on having pride in yourself")
    recommendation = (f"The Self-Esteem range of {round(SE_value)} is very good according to the Healthwatch Suffolk website.I would recommend to keep on having pride in yourself") #Suggest this
elif SE_value < 5 and mean_value > 3: #If the range value between 3 and 5
    #print("The Self-Esteem range is okay but I recommend for people to increase their confidence level a bit more.")
    recommendation = (f"The Self-Esteem range of {round(SE_value)} is okay according to the Healthwatch Suffolk website. The ideal range is 3-5 (according to the Healthwatch Suffok). It is an okay value but I recommend for people to increase their confidence level a bit more.") #Suggest the recommendation
else: #If Self-Esteem value is lower than 3
    #print("That is a very low Self-Esteem value. I recommend increasing confidence levels ASAP")
    recommendation = (f" {round(SE_value)} is a very low Self-Esteem value according to the Healthwatch Suffolk website. I recommend increasing confidence levels ASAP") #suggest this idea
print(f"I say {recommendation}") #Display the suggestion

#Getting the mean value manually
mean_SE = df['SE (self esteem)'] #Gets the column with the BMI values
average = sum(mean_SE)/len(mean_SE) #Finds the average number of the value
print(f"The mean value for the The self esteem column is {round(average)}") #Displays the number, rounded


#Getting the median value manually
median_SE = df['SE (self esteem)'].tolist() #Gets the column 'SE' and makes it as a list
median_SE.sort() #Sorts the list

if len(median_SE) % 2 == 0: #If the remander of the lenght of the list is zero
    middle_plus_one = len(median_SE) // 2 #Divide the lenght of list by 2
    median = (median_SE[middle_plus_one - 1] + median_SE[middle_plus_one]) / 2 #Finds the median value of the list
else: #Else
    middle = len(median_SE) // 2 #Floor divide the list by 2
    median = median_SE[middle] #Assign the middle value of the list to a variable
print(f"The middle value for SE (self esteem) is {round(median)}") #Display the value in the variable rounded

#BR3
#file for making graphs
df['SE (self esteem)'] = df.iloc[1:10][['SE (self esteem)']] #Gets the first few values from the column 'SE (self esteem) in datset
df['YEAR'] = df.iloc[1:10][['YEAR']] #Gets the first few values from the column 'YEAR' in dataset
df['ESTIMATE'] = df.iloc[1:11][['ESTIMATE']] #Gets the first few values from column 'ESTIMATE' in dataset
df['AGE'] = df.iloc[1:11]['AGE'] #Gets the first few values from column 'AGE' in dataset



df.to_csv('shortened_data1.csv') #Reads this information into a new csv file

#Line chart
df = pd.read_csv('shortened_data1.csv') #Reads the new dataset
line_chart = px.line(df, x= 'YEAR', y='SE (self esteem)', title='Self Esteem of People') #Using plotly to create a line chart using the years and self-esteem from dataset
#line_chart.show() #Displays figure
line_chart_on_html = line_chart.to_html(full_html = False, include_plotlyjs = 'cdn') #Makes the graph be displayed on a website


#Bar Chart
df = pd.read_csv('shortened_data1.csv') #Reads the new dataset
bar_chart = px.bar(df, x='YEAR', y='ESTIMATE',
             labels = {'YEAR':'YEARS', 'ESTIMATE':'BMI (Body Mass Index'},
             title = 'Estimated Weight of people over the years') #Makes a bar chart with x-axis,y=axis and title
#bar_chart.show() #Displays the graph
bar_chart_on_html = bar_chart.to_html(full_html = False, include_plotlyjs = 'cdn') #Makes the graph be displayed on a website


#Pie Chart for BMI aged 20
df = pd.read_csv('shortened_data1.csv') #Reads the new dataset
pie_chart = px.pie(df, #Creates a pie chart using data from the dataset
             values='AGE', #Gives the values for the pie chart
             names='ESTIMATE', #Gives the different BMI index rates
             title='BMI of people of different people aged 20') #Gives the pie chart a label
#pie_chart.show() #Displays graph
pie_chart_on_html = pie_chart.to_html(full_html = False, include_plotlyjs = 'cdn') #Makes the graph be displayed on a website

#BR3/#AR1
app = Flask(__name__) #Creates a website

#Pie chart for Self-Esteem
df = pd.read_csv('shortened_data1.csv') #Reads the new dataset
pie_chart2 = px.pie(df, #Creates a pie chart using data from the dataset
             values='AGE', #Gives the values for the pie chart
             names='SE (self esteem)', #Gives the different BMI index rates
             title='Self Esteem of people of different people') #Gives the pie chart a label
#pie_chart2.show() #Displays graph
pie_chart2_on_html = pie_chart2.to_html(full_html = False, include_plotlyjs = 'cdn') #Makes the graph be displayed on a website


@app.route("/") #Creates an app route
def index(): #Makes a function
    return render_template( #Returns a rendered version of the following
        'index.html', #From the file 'index.html'
         line_chart = line_chart_on_html, #Displays the line chart on website
         bar_chart = bar_chart_on_html, #Displays the bar chart on website
         pie_chart = pie_chart_on_html, #Displays the pie chart on website
         pie_chart2 = pie_chart2_on_html #Displays the pie chart on website
    )

@app.route('/page_1') #Creates a new route 
def index1(): #Creates function
    return render_template('page1.html') #Returns what is in the file 'page1.html'

@app.route('/last_page') #Creates another web page on the same website
def index2(): #Creates a function
    return render_template( #Displays information on the final page
        'final_page.html',
        suggestions = suggestions, #Moves the suggestion to the website
        recommendation = recommendation, #Moves the suggestions to the website
    ) 

if __name__ == '__main__': #If name is equal to main
    app.run(host='0.0.0.0', port=5001, debug=False) #Runs the website
