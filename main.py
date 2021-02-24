#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Francis Yap Jun Ting>
#Group Name: <PythonOkay>
#Class: <PN2004K>
#Date: <2/17/2021>
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
import pandas as pd
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas for data analysis
#import matplotlib for pie chart
import matplotlib.pyplot as plt
#count of each of the elements present in the container
from collections import Counter
#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
    def __init__(self):

        #load excel data (CSV format) to dataframe - 'df'
        dataframe = pd.read_csv('MonthyVisitors.csv')
        #show specific country dataframe
        sortCountry(dataframe)

        
#########################################################################
#CLASS Branch: End of Code
#########################################################################

#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

    #print number of rows in dataframe
    print("There are " + str(len(df)) + " data rows read. \n")

    #display dataframe (rows and columns)
    print("The following dataframe are read as follows: \n")
    print(df)

    #display a specific country (Australia) in column #33
    country_label = df.columns[33]
    print("\n\n" + country_label + "was selected.")

    #display a sorted dataframe based on selected country
    print(" The" + country_label + "was sorted in ascending order. \n")
    sorted_df =df.sort_values(country_label,ascending=[0])
    print(sorted_df)

  
    #locate the data of the selected countries
    df = df.iloc[204:324, 2:9]
    #print(df) to check whether its working
    print(df) 

    
    #create variables
    visitor = []
    country =  []
    total_visitors = []
    country_dictionary = {}
    

    #df.columns to read it top to bottom instead of reading the entire thing
    for countries in df.columns[0:8]:
        country.append(countries)
        for visitors in df[countries]:
            visitor.append(visitors)


    #change str to int else they would not able calculate them 
    for i in range(0, len(visitor)):
      if visitor[i] == " na ":
        visitor[i] = 0
      else:
        visitor[i] = int(visitor[i])
    numbers = len(visitor)
    #counters to count how many number you have in a row
    counters = numbers / len(country)
    index1 = 0
    #convert the numbers that the counters find into int
    index2 = int(counters)


    #total_visitors.append allows you to add the amount of lines and the total amount of visitors in the 100 lines together
    for countries in range(0, len(country)):
        total_visitors.append(sum(visitor[index1:index2]))
        #converts the counters into int
        index1 = index1 + int(counters)
        index2 = index2 + int(counters)

    
    country_dictionary = {
        country[i]: total_visitors[i]
        for i in range(len(country))
    }

    #sort the number of visitors in one entire country and add everything together
    sort_visitor_dict = sorted(country_dictionary.items(),
                              key = lambda x: x[1],
                              reverse=True)
  

    country_dictionary = dict(sort_visitor_dict)

    k =Counter(country_dictionary)

    Top_3_Visitor = k.most_common(3)
    # allows you to create a list and collate the amount of countries that you have with the highest amount of visitors and show the top 3
    df = pd.DataFrame(Top_3_Visitor,columns=["Countries", "Visitors"])


    print(df)

    labels = []
    sizes = []

    #Get data from excel for countries
    for x in df["Countries"]:
      labels.append(x)
    for y in df["Visitors"]:
      sizes.append(y)
    
    #create variables
    distance = 0.1
    separate = []

    for i in range(0, len(df['Visitors'])):
      separate.append(distance)

    
    #autopct changes to display percentage in 2dp , explode is the distance between the pie chart, shadow=True means that you want a shadow behind the piechart
    plt.pie(sizes,labels=labels, explode=separate, startangle=90, autopct='%1.2f%%',shadow=True)
    plt.axis('equal')

    #The location of the legend
    plt.legend(loc="best")

    #plt.show() starts an event loop, looks for all currently active figure objects, and opens one or more interactive windows that display your figure or figures.
    plt.show()
    



  
#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':
  
   #Project Title
   print('######################################')
   print('# Data Analysis App - PYTHON Project #')
   print('######################################')

  #perform data analysis on specific excel (CSV) file
   DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################