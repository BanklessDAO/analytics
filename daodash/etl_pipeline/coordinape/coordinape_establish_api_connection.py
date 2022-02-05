import requests
from pprint import pprint
import os
import pandas as pd

# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

# api endpoints, authorization & header
auth_token = os.environ.get('AUTH_TOKEN')
api_endpoint_manifest_bb = os.environ.get('API_ENDPOINT_MANIFEST_BB')
api_endpoint_users_bankless = os.environ.get('API_ENDPOINT_USERS_BANKLESS')
api_endpoint_users_protocol_bankless = os.environ.get(
    'API_ENDPOINT_USERS_PROTOCOL_BANKLESS')

api_endpoint_manifest_circle_bankless = os.environ.get(
    'API_ENDPOINT_MANIFEST_CIRCLE_BANKLESS')

api_endpoint_manifest_protocol_bankless = os.environ.get(
    'API_ENDPOINT_MANIFEST_PROTOCOL_BANKLESS')

HEADER = {'Authorization': f'{auth_token}'}

# --- Primary steps to explore nested data ------
response = requests.get(
    f'{api_endpoint_manifest_circle_bankless}', headers=HEADER)
result = response.json()
dataframe = pd.json_normalize(result)
list_of_column_names = list(dataframe)

# dataframe is [1 rows x 48 columns]
# unpack dataframe using f-string
for item in list_of_column_names:
    print(dataframe[f'{item}'])

# ------------------------------------------------

# specific api endpoint
response = requests.get(
    f'{api_endpoint_manifest_circle_bankless}', headers=HEADER)
response_2 = requests.get(f'{api_endpoint_users_bankless}', headers=HEADER)
response_3 = requests.get(
    f'{api_endpoint_users_protocol_bankless}', headers=HEADER)

response_4 = requests.get(
    f'{api_endpoint_manifest_protocol_bankless}', headers=HEADER)

# incoming data as json
result = response.json()
result_2 = response_2.json()
result_3 = response_3.json()
result_4 = response_4.json()

# normalize json data into dataframe
dataframe = pd.json_normalize(result)
dataframe_2 = pd.json_normalize(result_2)
dataframe_3 = pd.json_normalize(result_3)
dataframe_4 = pd.json_normalize(result_4)

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
use dataframe['circle.users']

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

# print columns names in dataframe_2 (api_endpoint_users_bankless)
for col in dataframe_2.columns:
    print(col)

"""
Column names in 'dataframe_2' (bankless coordinape circle, users api endpoint)

id
name
address
give_token_received
give_token_remaining
role
non_receiver
circle_id
created_at
updated_at
bio
epoch_first_visit
non_giver
deleted_at
starting_tokens
fixed_non_receiver
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
"""

# print columns names in dataframe_3 (api_endpoint_users_protocol_bankless)
for col in dataframe_3.columns:
    print(col)

"""
source: dataframe_3 api_endpoint_users_protocol_bankless

name
address
circle_id
give_token_received
give_token_remaining
bio
non_receiver
epoch_first_visit
non_giver
protocol_id
role
starting_tokens
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
"""

# print columns names in dataframe_4 (api_endpoint_manifest_protocol_bankless)
for col in dataframe_4.columns:
    print(col)

"""
dataframe_4: api_endpoint_manifest_protocol_bankless

myUsers *
circles *
active_epochs
profile.id *
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
profile.address    *
profile.created_at  *
profile.updated_at
profile.admin_view
profile.ann_power
circle.nominees    
circle.users       *
circle.token_gifts  *
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
list_of_column_names_3 = list(dataframe_3)
list_of_column_names_4 = list(dataframe_4)

for item in list_of_column_names_3:
    print(dataframe_3[f'{item}'])

print(dataframe_3['name'], dataframe_3['address'], dataframe_3['circle_id'], dataframe_3['protocol_id'],
      dataframe_3['profile.id'], dataframe_3['profile.discord_username'], dataframe_3['profile.address'], dataframe_3['profile.created_at'])

for item in list_of_column_names_4:
    print(dataframe_4[f'{item}'])

# ------ Explore participants in "Bankless" Circle_id 24 -------

# start with protocol_id, dataframe_3, api_endpoint_users_protocol_bankless

# select unique circle_id
# dataframe_3['circle_id'].unique()

# query circle.users of *each* circle_id: [ 24,  63, 305, 492, 878]
# concat
