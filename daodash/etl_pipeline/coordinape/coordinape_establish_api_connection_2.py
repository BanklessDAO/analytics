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

api_endpoint_manifest_protocol_bankless = os.environ.get(
    'API_ENDPOINT_MANIFEST_PROTOCOL_BANKLESS')

response = requests.get(
    f'{api_endpoint_manifest_protocol_bankless}', headers=HEADER)

result = response.json()

# normalize json data into dataframe
dataframe = pd.json_normalize(result)

# print dataframe
print(dataframe)

for c in dataframe.columns:
    print(dataframe[f'{c}'])

"""
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
circle.circle.name             --- "bankless"
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

for d in dataframe['circles'][0]:
    print(d['id'], d['name'], d['protocol_id'])

for d in dataframe['active_epochs'][0]:
    print(d)
