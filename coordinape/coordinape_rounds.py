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

# ----- Data Endpoints

# Coordinape Round -- OG Bankless(June): Circle id 24
response24 = requests.get(
    'https://api.coordinape.com/api/v2/token-gifts?circle_id=24', headers=HEADER)

# return list of 7135 dictionaries
result24 = response24.json()
# use pandas to convert list of dict to dataframe
df24 = pd.json_normalize(result24)


# Coordinape Round -- Bankless L1: Circle id 305
response305 = requests.get(
    'https://api.coordinape.com/api/v2/token-gifts?circle_id=305', headers=HEADER)

# return & convert list of dict to dataframe using pandas
result305 = response305.json()
df305 = pd.json_normalize(result305)


# Coordinape Round -- Bankless L2: Circle id 492
response492 = requests.get(
    'https://api.coordinape.com/api/v2/token-gifts?circle_id=492', headers=HEADER)
result492 = response492.json()
df492 = pd.json_normalize(result492)


# Coordinape Round -- Bankless GP: Circle id 878
response878 = requests.get(
    'https://api.coordinape.com/api/v2/token-gifts?circle_id=878', headers=HEADER)
result878 = response878.json()
df878 = pd.json_normalize(result878)

# concatenate dataframes
frames = [df24, df305, df492, df878]
concat_frames = pd.concat(frames)

# reset index twice
concat_frames_2 = concat_frames.reset_index()
concat_frames_3 = concat_frames_2.reset_index()

# select specific columns
concat_frames_4 = concat_frames_3[['level_0', 'id', 'recipient_address', 'sender_address',
                                   'recipient_id', 'sender_id', 'tokens', 'circle_id', 'epoch_id',
                                   'dts_created']]

# change column name 'dts_created' -> 'timestamp'
concat_frames_5 = concat_frames_4.rename(
    columns={'level_0': 'id', 'id': 'coord_id', 'dts_created': 'timestamp'}, inplace=False)
print(concat_frames_5)

# write to csv
# concat_frames_5.to_csv('coordinape_pipe_v1.csv')
