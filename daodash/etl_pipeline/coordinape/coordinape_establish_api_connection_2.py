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


# make requests to api endpoint and print a dataframe
# then, perform a basic loop to print something out

def send_request():
    """Description

    Send request to Coordinape API endpoint.
    Return json object of the response.

    Args: None.

    Returns: json object

    Notes:
    """
    response = requests.get(
        f'{api_endpoint_manifest_protocol_bankless}', headers=HEADER)
    return response.json()


def normalize(result):
    """Description

    Takes json object and normalizes into dataframe

    Args: json object

    Returns: dataframe
    Raises/Notes:
    """
    dataframe = pd.json_normalize(result)
    return dataframe


def print_columns(df):
    """Description

    Loop through dataframe column names
    Use names to index through dataframe and print each column

    Args: dataframe

    Returns: print dataframe indexed by column name
    Raises/Notes:
    """
    for col in df.columns:
        print(df[f'{col}'])
    print('\n')


def print_circles(df):
    """Description:

    Loop through 'circles' column, a list of dictionaries,
    print values associated with the keys: id, name, protocol_id

    Args: dataframe

    Returns:
    Raises/Notes:
    """
    for dct in df['circles'][0]:
        print(dct['id'], dct['name'], dct['protocol_id'])
    print('\n')


result = send_request()
df = normalize(result)
print_columns(df)
print_circles(df)


"""
dataframe column names:

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
