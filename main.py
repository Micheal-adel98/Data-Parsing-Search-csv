# import pandas as pd

# df = pd.read_csv('Movie-Dataset-Latest (1).csv')
# df.to_json('Movie-Dataset-Latest.json')

import csv
import json
import xmltodict
import pandas as pd

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(convFilePath, jsonFilePath):
	
    if convFilePath.split('.')[1] == 'csv':
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
            


    elif convFilePath.split('.')[1] == 'xml':
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
                
    elif convFilePath.split('.')[1] == 'xlsx':
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

