from email import header
import requests
from pprint import pprint
import os
import pandas as pd

# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

# api endpoints, authorization & header
auth_token = os.environ.get('AUTH_TOKEN')
api_endpoint_manifest = os.environ.get('API_ENDPOINT_MANIFEST')
api_endpoint_users = os.environ.get('API_ENDPOINT_USERS')
HEADER = {'Authorization': f'{auth_token}'}

# specific api endpoint
response = requests.get(f'{api_endpoint_manifest}', headers=HEADER)
response_2 = requests.get(f'{api_endpoint_users}', headers=HEADER)

# incoming data as json
result = response.json()
result_2 = response_2.json()

# normalize json data into dataframe
dataframe = pd.json_normalize(result)
dataframe_2 = pd.json_normalize(result_2)

# print dataframe
print(dataframe)
print(dataframe_2)

# print column names
print(dataframe.columns)
print(dataframe_2.columns)

# Note; each column is a potential list of dictionaries
print(type(dataframe.iloc[:, 0][0]))      # list
print(len(dataframe.iloc[:, 0][0]))       # list containing 5 dictinoaries
print(type(dataframe.iloc[:, 0][0][0]))   # dictionaries

# examples from manifest endpoint
pprint(dataframe['myUsers'][0][0]['name'])
pprint(dataframe['myUsers'][0][0]['teammates'])

teammates_list = dataframe['myUsers'][0][0]['teammates']

# find teammates for a given user in a given circle
for i in teammates_list:
    print(i['name'], i['address'])
