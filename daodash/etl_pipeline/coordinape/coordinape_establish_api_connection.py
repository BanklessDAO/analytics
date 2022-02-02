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

# --- Primary steps to explore nested data ------
response = requests.get(f'{api_endpoint_manifest}', headers=HEADER)
result = response.json()
dataframe = pd.json_normalize(result)
list_of_column_names = list(dataframe)

# dataframe is [1 rows x 48 columns]
# unpack dataframe using f-string
for item in list_of_column_names:
    print(dataframe[f'{item}'])

# ------------------------------------------------

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

# alternative way to print column names
pprint(list(dataframe))

# print columns names
for col in dataframe.columns:
    print(col)

# Note; each column is a potential list of dictionaries
print(type(dataframe.iloc[:, 0][0]))      # list
print(len(dataframe.iloc[:, 0][0]))       # list containing 5 dictinoaries
print(type(dataframe.iloc[:, 0][0][0]))   # dictionaries

# examples from manifest api endpoint
pprint(dataframe['myUsers'][0][0]['name'])
pprint(dataframe['myUsers'][0][0]['teammates'])

teammates_list = dataframe['myUsers'][0][0]['teammates']

# find teammates for a given user in a given circle
for i in teammates_list:
    print(i['name'], i['address'])


# print columns names
for col in dataframe.columns:
    print(col)

"""
Column names in 'dataframe':

myUsers
circles
active_epochs
profile.id
profile.avatar
profile.background
profile.skills
profile.bio
profile.telegram_username
profile.discord_username
profile.twitter_username
profile.github_username
profile.medium_username
profile.website
profile.address
profile.created_at
profile.updated_at
profile.admin_view
profile.ann_power
circle.nominees
circle.users
circle.token_gifts
circle.pending_gifts
circle.epochs
circle.circle.id
circle.circle.name
circle.circle.created_at
circle.circle.updated_at
circle.circle.protocol_id
circle.circle.token_name
circle.circle.team_sel_text
circle.circle.alloc_text
circle.circle.logo
circle.circle.vouching
circle.circle.min_vouches
circle.circle.nomination_days_limit
circle.circle.vouching_text
circle.circle.default_opt_in
circle.circle.team_selection
circle.circle.only_giver_vouch
circle.circle.is_verified
circle.circle.auto_opt_out
circle.circle.protocol.id
circle.circle.protocol.name
circle.circle.protocol.created_at
circle.circle.protocol.updated_at
circle.circle.protocol.telegram_id
circle.circle.protocol.is_verified
"""

# working with nested json
# need to get to item *in* list of dictionaries to use with json_normalize to produce flatten datafame
# json_normalize() used once already :: dataframe = pd.json_normalize(result)

pd.json_normalize(dataframe['myUsers'][0])
pd.json_normalize(dataframe['circles'][0])
pd.json_normalize(dataframe['circle.users'][0])
pd.json_normalize(dataframe['circle.token_gifts'][0])

# normalize into dataframe, then list column names
token_gifts = pd.json_normalize(dataframe['circle.token_gifts'][0])
print(list(token_gifts))

# The Coordinape API produces nested data
# Here's the TLDR

list_of_column_names = list(dataframe)
