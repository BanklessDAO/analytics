import requests
from pprint import pprint
import os
import pandas as pd

# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

# authorization & header
auth_token = os.environ.get('AUTH_TOKEN')
HEADER = {'Authorization': f'{auth_token}'}

# Coordinape Round -- OG Bankless(June): Circle id 24
# n = 299
response24 = requests.get(
    'https://api.coordinape.com/api/v2/users?circle_id=24', headers=HEADER)
result24 = response24.json()
df24 = pd.json_normalize(result24)
# pprint(df.columns)
df24_a = pd.DataFrame(
    {
        "name": df24['name'],
        "discord_username": df24['profile.discord_username'],
        "address": df24['address'],
        "circle_id": df24['circle_id']
    }
)

# Coordinape round --Bankless L1: Circle id 305
# n = 169
response305 = requests.get(
    'https://api.coordinape.com/api/v2/users?circle_id=305', headers=HEADER)
result305 = response305.json()
df305 = pd.json_normalize(result305)
# pprint(df.columns)
df305_a = pd.DataFrame(
    {
        "name": df305['name'],
        "discord_username": df305['profile.discord_username'],
        "address": df305['address'],
        "circle_id": df305['circle_id']
    }
)

# Coordinape round --Bankless L1: Circle id 492
# n = 169
response492 = requests.get(
    'https://api.coordinape.com/api/v2/users?circle_id=492', headers=HEADER)
result492 = response492.json()
df492 = pd.json_normalize(result492)
# pprint(df.columns)
df492_a = pd.DataFrame(
    {
        "name": df492['name'],
        "discord_username": df492['profile.discord_username'],
        "address": df492['address'],
        "circle_id": df492['circle_id']
    }
)

# Coordinape round --Bankless L1: Circle id 878
# n = 356
response878 = requests.get(
    'https://api.coordinape.com/api/v2/users?circle_id=878', headers=HEADER)
result878 = response878.json()
df878 = pd.json_normalize(result878)
# pprint(df.columns)
df878_a = pd.DataFrame(
    {
        "name": df878['name'],
        "discord_username": df878['profile.discord_username'],
        "address": df878['address'],
        "circle_id": df878['circle_id']
    }
)

# concatenate dataframes
frames = [df24_a, df305_a, df492_a, df878_a]
concat_frames = pd.concat(frames)

# reset index
concat_frames_2 = concat_frames.reset_index()
concat_frames_3 = concat_frames_2.reset_index()

# select specific colums
concat_frames_4 = concat_frames_3[[
    'level_0', 'name', 'discord_username', 'address', 'circle_id']]

# change column name 'level_0' -> 'id'
concat_frames_5 = concat_frames_4.rename(
    columns={'level_0': 'id'}, inplace=False)

print(concat_frames_5)

# write to csv
# concat_frames_5.to_csv('coordinape_name_address.csv')

#response = requests.get('https://api.coordinape.com/api/v2/manifest?circle_id=63', headers=HEADER)

# pprint(df['myUsers'][0])
# df['myUsers'][0][0] -- paul and teammates for circle_id: 24
# df['myUsers'][0][1] -- paul and teammates for circle_id: 878
