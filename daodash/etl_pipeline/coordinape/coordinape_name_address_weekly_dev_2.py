import requests
from pprint import pprint
import os
import pandas as pd

# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

# api endpoints, authorization & header

auth_token = os.environ.get('AUTH_TOKEN')
HEADER = {'Authorization': f'{auth_token}'}

# go to protocol_id = 15 (bankless)
# find all circles (participated in), belonging to protocol_id = 15 (bankless)
api_endpoint_users_protocol_bankless = os.environ.get(
    'API_ENDPOINT_USERS_PROTOCOL_BANKLESS')

# go to manifest circle id [ 24,  63, 305, 492, 878]
# these are circles i participated in

api_endpoint_users_circle_bankless = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_BANKLESS')

api_endpoint_users_circle_bb = os.environ.get('API_ENDPOINT_USERS_CIRCLE_BB')

api_endpoint_users_circle_l1 = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_L1')

api_endpoint_users_circle_l2 = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_L2')

api_endpoint_users_circle_gp = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_GP')

# response, requests for api endpoints
response_user_protocol = requests.get(
    f'{api_endpoint_users_protocol_bankless}', headers=HEADER)

response_users_circle_bankless = requests.get(
    f'{api_endpoint_users_circle_bankless}', headers=HEADER)

response_users_circle_bb = requests.get(
    f'{api_endpoint_users_circle_bb}', headers=HEADER)

response_users_circle_l1 = requests.get(
    f'{api_endpoint_users_circle_l1}', headers=HEADER)

response_users_circle_l2 = requests.get(
    f'{api_endpoint_users_circle_l2}', headers=HEADER)

response_users_circle_gp = requests.get(
    f'{api_endpoint_users_circle_gp}', headers=HEADER)

# incoming json data
result_user_protocol = response_user_protocol.json()
result_circle_bankless = response_users_circle_bankless.json()
result_circle_bb = response_users_circle_bb.json()
result_circle_l1 = response_users_circle_l1.json()
result_circle_l2 = response_users_circle_l2.json()
result_circle_gp = response_users_circle_gp.json()

# normalize json data into dataframe
df_user_protocol = pd.json_normalize(result_user_protocol)
df_circle_bankless = pd.json_normalize(result_circle_bankless)
df_circle_bb = pd.json_normalize(result_circle_bb)
df_circle_l1 = pd.json_normalize(result_circle_l1)
df_circle_l2 = pd.json_normalize(result_circle_l2)
df_circle_gp = pd.json_normalize(result_circle_gp)

print(df_user_protocol)
print(df_circle_bankless)
print(df_circle_bb)
print(df_circle_l1)
print(df_circle_l2)
print(df_circle_gp)

# select unique circle_id
# array([ 24,  63, 305, 492, 878])
df_user_protocol['circle_id'].unique()

# circle_id 24 'bankless'
df_circle_bankless_a = pd.DataFrame(
    {
        "name": df_circle_bankless['name'],
        "discord_username": df_circle_bankless['profile.discord_username'],
        "address": df_circle_bankless['address'],
        "circle_id": df_circle_bankless['circle_id'],
        "circle_name": "bankless"
    }
)

# circle_id 63 'BanklessDAO Bounty Board'
df_circle_bb_a = pd.DataFrame(
    {
        "name": df_circle_bb['name'],
        "discord_username": df_circle_bb['profile.discord_username'],
        "address": df_circle_bb['address'],
        "circle_id": df_circle_bb['circle_id'],
        "circle_name": "BanklessDAO Bounty Board"
    }
)

# circle_id 305 'L1'
df_circle_l1_a = pd.DataFrame(
    {
        "name": df_circle_l1['name'],
        "discord_username": df_circle_l1['profile.discord_username'],
        "address": df_circle_l1['address'],
        "circle_id": df_circle_l1['circle_id'],
        "circle_name": "L1"
    }
)

# circle_id 492 'L2'
df_circle_l2_a = pd.DataFrame(
    {
        "name": df_circle_l2['name'],
        "discord_username": df_circle_l2['profile.discord_username'],
        "address": df_circle_l2['address'],
        "circle_id": df_circle_l2['circle_id'],
        "circle_name": "L2"
    }
)

# circle_id 878 'Guest Pass'
df_circle_gp_a = pd.DataFrame(
    {
        "name": df_circle_gp['name'],
        "discord_username": df_circle_gp['profile.discord_username'],
        "address": df_circle_gp['address'],
        "circle_id": df_circle_gp['circle_id'],
        "circle_name": "Guest Pass"
    }
)

# concatenate dataframe
# length of concat_frame == length of df_user_protocol['name']
frame = [df_circle_bankless_a, df_circle_bb_a,
         df_circle_l1_a, df_circle_l2_a, df_circle_gp_a]
concat_frames = pd.concat(frame)

# reset index
concat_frames_2 = concat_frames.reset_index()
concat_frames_3 = concat_frames_2.reset_index()

# select specific columns
concat_frames_4 = concat_frames_3[[
    'level_0', 'name', 'discord_username', 'address', 'circle_id', 'circle_name']]

# change column name
concat_frames_5 = concat_frames_4.rename(
    columns={'level_0': 'id'}, inplace=False)

# write to csv
# concat_frames_5.to_csv('coordinape_name_address_2.csv')

# --------- comparison to concat_frames -----------
df_user_protocol_a = pd.DataFrame(
    {
        "name": df_user_protocol['name'],
        "discord_username": df_user_protocol['profile.discord_username'],
        "address": df_user_protocol['address'],
        "circle_id": df_user_protocol['circle_id']
    }
)
