#We import our dictionaries which gives it's codes specific functions and use.
#Note: Jupyter is case sensitive
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#This is the total covid-19 cases recorded by the WHO and grouped based on regions to capture all the countries
Data_Covid = pd.read_csv(r'C:\Users\Samuel Okachi\Documents Covid 19 Data.csv')
Data_Covid

#Define a function for our data
#My dataframe contains the grouped countries in the WHO regions in the world
#Here each countries are grouped under specified headers according to the Covid-19 cases
def retrieve_data(url):
    data = pd.read_csv(url)
    return data
df_world = retrieve_data("worldometer_data.csv")
Data_covid = retrieve_data("Covid 19 Data.csv")
print(df_world)

#My Dataframe contains data that were recorded each day since the beginning of the covid-19 pandemic
#The recorded are based on days of each month
#Data are grouped in terms of Confirmed Cases, Recovered, Active,New cases and New deahts
df_day = pd.read_csv("day_wise.csv")
print(df_day)

groups = df_world.groupby(['WHO Region'])['ActiveCases','TotalDeaths'].sum()
groups = groups.reset_index()
groups

y_axis = groups['WHO Region']
x_axis = groups['ActiveCases']
title = "Covid-19 Active Cases "
x_label = "Health Regions"
y_label = "Active Cases"

#Here i plot our Bar_chart 
def create_bar_chart(y_axis, x_axis, title, x_label, y_label):
    plt.figure(figsize =(15,15))
    plt.bar(y_axis,x_axis,color="g")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    plt.savefig("bar_chart.pdf")
create_bar_chart(y_axis, x_axis, title, x_label, y_label)
   
#Here i give a digrammatic representation using Pie Chart
#Define a Function 
label = ['Europe','Africa','Americas', 'Eastern Mediterranean', 'Western Pacific', 'South-EastAsia']
countries = [55,47,35,22,15,10]
explodes = [0.1, 0, 0, 0, 0, 0,]
title = ('WHO Region')

def create_pie_chart(countries,explodes, label):
    plt.pie(countries,labels=label, explode=explodes, autopct='%.1f%%', shadow=True)
    plt.title('WHO Regions')
    plt.show()
    plt.savefig("pie_chart.png")

create_pie_chart(countries,explodes,label)

#Line plot 
#This line plot shows the amount of TotalDeaths and ActiveCases for the entire WHO Regions
groups.plot()

