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

# go to user circle ids [24, 63, 117, 1371, 1489, 969, 921, 113, 2061]

api_endpoint_users_circle_bankless = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_BANKLESS')

api_endpoint_users_circle_bb = os.environ.get('API_ENDPOINT_USERS_CIRCLE_BB')

api_endpoint_users_circle_av = os.environ.get('API_ENDPOINT_USERS_CIRCLE_AV')

api_endpoint_users_cirlce_intl_media_node = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_INTL_MEDIA_NODE')

api_endpoint_users_circle_translators_guild = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_TRANSLATORS_GUILD')

api_endpoint_users_circle_dev_guild = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_DEV_GUILD')

api_endpoint_users_circle_bankless_consulting = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_BANKLESS_CONSULTING')

api_endpoint_users_circle_design_guild = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_DESIGN_GUILD')

api_endpoint_users_circle_research_guild = os.environ.get(
    'API_ENDPOINT_USERS_CIRCLE_RESEARCH_GUILD')

# response, requests for api endpoints

response_users_circle_bankless = requests.get(
    f'{api_endpoint_users_circle_bankless}', headers=HEADER)

response_users_circle_bb = requests.get(
    f'{api_endpoint_users_circle_bb}', headers=HEADER)

response_users_circle_av = requests.get(
    f'{api_endpoint_users_circle_av}', headers=HEADER)

response_users_circle_intl_media_node = requests.get(
    f'{api_endpoint_users_cirlce_intl_media_node}', headers=HEADER)

response_users_circle_translators_guild = requests.get(
    f'{api_endpoint_users_circle_translators_guild}', headers=HEADER)

response_users_circle_dev_guild = requests.get(
    f'{api_endpoint_users_circle_dev_guild}', headers=HEADER)

response_users_circle_bankless_consulting = requests.get(
    f'{api_endpoint_users_circle_bankless_consulting}', headers=HEADER)

response_users_circle_design_guild = requests.get(
    f'{api_endpoint_users_circle_design_guild}', headers=HEADER)

response_users_circle_research_guild = requests.get(
    f'{api_endpoint_users_circle_research_guild}', headers=HEADER)

# income json data
result_circle_bankless = response_users_circle_bankless.json()
result_circle_bb = response_users_circle_bb.json()
result_circle_av = response_users_circle_av.json()
result_circle_intl_media_node = response_users_circle_intl_media_node.json()
result_circle_translators_guild = response_users_circle_translators_guild.json()
result_circle_dev_guild = response_users_circle_dev_guild.json()
result_circle_bankless_consulting = response_users_circle_bankless_consulting.json()
result_circle_design_guild = response_users_circle_design_guild.json()
result_circle_research_guild = response_users_circle_research_guild.json()

# normalize json data into dataframe
df_circle_bankless = pd.json_normalize(result_circle_bankless)
df_circle_bb = pd.json_normalize(result_circle_bb)
df_circle_av = pd.json_normalize(result_circle_av)
df_circle_intl_media_node = pd.json_normalize(result_circle_intl_media_node)
df_circle_translators_guild = pd.json_normalize(
    result_circle_translators_guild)
df_circle_dev_guild = pd.json_normalize(result_circle_dev_guild)
df_circle_bankless_consulting = pd.json_normalize(
    result_circle_bankless_consulting)
df_circle_design_guild = pd.json_normalize(result_circle_design_guild)
df_circle_research_guild = pd.json_normalize(result_circle_research_guild)

# go to user circle ids [24, 63, 117, 1371, 1489, 969, 921, 113, 2061]

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

# circle_id 117 'AV Guild'
df_circle_av_a = pd.DataFrame(
    {
        "name": df_circle_av['name'],
        "discord_username": df_circle_av['profile.discord_username'],
        "address": df_circle_av['address'],
        "circle_id": df_circle_av['circle_id'],
        "circle_name": "AV Guild"
    }
)

# circle_id 1371 'Intl Media Node'
df_circle_intl_media_node_a = pd.DataFrame(
    {
        "name": df_circle_intl_media_node['name'],
        "discord_username": df_circle_intl_media_node['profile.discord_username'],
        "address": df_circle_intl_media_node['address'],
        "circle_id": df_circle_intl_media_node['circle_id'],
        "circle_name": "Intl Media Node"
    }
)

# circle_id 1489 'Translators Guild'
df_circle_translators_guild_a = pd.DataFrame(
    {
        "name": df_circle_translators_guild['name'],
        "discord_username": df_circle_translators_guild['profile.discord_username'],
        "address": df_circle_translators_guild['address'],
        "circle_id": df_circle_translators_guild['circle_id'],
        "circle_name": "Translators Guild"
    }
)

# circle_id 969 'Dev Guild'
df_circle_dev_guild_a = pd.DataFrame(
    {
        "name": df_circle_dev_guild['name'],
        "discord_username": df_circle_dev_guild['profile.discord_username'],
        "address": df_circle_dev_guild['address'],
        "circle_id": df_circle_dev_guild['circle_id'],
        "circle_name": "Dev Guild"
    }
)

# circle_id 921 'Bankless Consulting'
df_circle_bankless_consulting_a = pd.DataFrame(
    {
        "name": df_circle_bankless_consulting['name'],
        "discord_username": df_circle_bankless_consulting['profile.discord_username'],
        "address": df_circle_bankless_consulting['address'],
        "circle_id": df_circle_bankless_consulting['circle_id'],
        "circle_name": "Bankless Consulting"
    }
)

# circle_id 113 'Design Guild'
df_circle_design_guild_a = pd.DataFrame(
    {
        "name": df_circle_design_guild['name'],
        "discord_username": df_circle_design_guild['profile.discord_username'],
        "address": df_circle_design_guild['address'],
        "circle_id": df_circle_design_guild['circle_id'],
        "circle_name": "Design Guild"
    }
)

# circle_id 2061 'Research Guild'
df_circle_research_guild_a = pd.DataFrame(
    {
        "name": df_circle_research_guild['name'],
        "discord_username": df_circle_research_guild['profile.discord_username'],
        "address": df_circle_research_guild['address'],
        "circle_id": df_circle_research_guild['circle_id'],
        "circle_name": "Research Guild"
    }
)

#print("df_circle_bankless: circle_id 24, Bankless")
# print(df_circle_bankless_a)

#print("df_circle_bb: circle_id 63, Bounty Board")
# print(df_circle_bb_a)

#print("df_circle_av: circle_id 117, AV Guild")
# print(df_circle_av_a)

#print("df_circle_intl_media_node: circle_id 1371, Intl Media Node")
# print(df_circle_intl_media_node_a)

#print("df_circle_translators_guild: circle_id 1489, Translators Guild")
# print(df_circle_translators_guild_a)

#print("df_circle_dev_guild: circle_id 969, Dev Guild")
# print(df_circle_dev_guild_a)

#print("df_circle_bankless_consulting: circle_id 921, Bankless Consulting")
# print(df_circle_bankless_consulting_a)

#print("df_circle_design_guild: circle_id 113, Design Guild")
# print(df_circle_design_guild_a)

#print("df_circle_research_guild: circle_id 2061, Research Guild")
# print(df_circle_research_guild_a)

# concatenate dataframe
frames = [df_circle_bankless_a, df_circle_bb_a, df_circle_av_a, df_circle_intl_media_node_a,
          df_circle_translators_guild_a, df_circle_dev_guild_a, df_circle_bankless_consulting_a,
          df_circle_design_guild_a, df_circle_research_guild_a]

concat_frames = pd.concat(frames)


# reset index
concat_frames_2 = concat_frames.reset_index()
concat_frames_3 = concat_frames_2.reset_index()


# select specific columns
concat_frames_4 = concat_frames_3[[
    'level_0', 'name', 'discord_username', 'address', 'circle_id', 'circle_name']]

# change column name
concat_frames_5 = concat_frames_4.rename(
    columns={'level_0': 'id'}, inplace=False)

print(concat_frames_5)
# write to csv or push to database
