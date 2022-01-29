from xmlrpc.client import boolean
import pandas as pd

# df = pd.read_csv('Movie-Dataset-Latest (1).csv')
# df.to_json('Movie-Dataset-Latest.json')

import csv
import json
import xmltodict
import pandas as pd

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(convFilePath, jsonFilePath):
	
    #check if file type is csv
    if convFilePath.split('.')[-1] == 'csv':
        # create a dictionary
        data = {}
        
        # Open a csv reader called DictReader
        with open(convFilePath, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)
           
            # Convert each row into a dictionary
            # and add it to data
            for rows in csvReader:
                
                # Assuming a column named 'No' to
                # be the primary key
                key = rows['No']
                data[key] = rows

        # Open a json writer, and use the json.dumps()
        # function to dump data
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))
            

    #check if file type is xml
    elif convFilePath.split('.')[-1] == 'xml':
        with open(convFilePath,"r") as xmlfileObj:
            #converting xml data to dictionary
            data_dict = xmltodict.parse(xmlfileObj.read())
            xmlfileObj.close()
            #creating JSON object using dictionary object  
            jsonObj= json.dumps(data_dict)
        
            #storing json data to json file
            with open(jsonFilePath, "w") as jsonfileObj:
                jsonfileObj.write(jsonObj)
                jsonfileObj.close()

    #check if file type is xlsx            
    elif convFilePath.split('.')[-1] == 'xlsx':
        excel_data_df = pd.read_excel(convFilePath)
        excel_data_df.to_json(jsonFilePath)
    else:
        print("File format not accepted")
# Driver Code

# Decide the two file paths according to your
# computer system
convFilePath = 'Movie-Dataset-Latest (1).csv'
jsonFilePath = 'Movie-Dataset-Latest.json'

# Call the make_json function
make_json(convFilePath, jsonFilePath)

def getData():
    df = pd.read_csv('Movie-Dataset-Latest (1).csv')
    print("which search u want ?")
    print("1- title")
    print("2- overview and release date")
    print('3- another column')
    choice = int(input("please enter number of choice: "))
    if choice == 1:
        value = input("enter value to search in title: ")
        print(df.loc[df['title']==value])

    elif choice == 2:
        overview = input("enter value to search in overview: ")
        date = input("enter value to search in release date: ")
        print(df[(df['overview']==overview) & (df['release_date']==date)])
    
    elif choice == 3:
        print(" No | id | title | release_date | overview | popularity | vote_average | vote_count | video")
        print(" please copy & paste column name")
        option = input('paste column name to search in: ')
        value = input('enter value: ')
        if option == 'No' or option == 'id' or option == "vote_count":
            value = int(value)
            print(df.loc[df[option]==value])
        elif option == "popularity" or option == "vote_average":
            value= float(value)
            print(df.loc[df[option]==value])
        elif option == "video":
            if  value == "FALSE":
                print(df)
            else:
                print("all video rows = FALSE")
    else:
        print("please check ur input")      

getData()
