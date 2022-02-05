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

api_manifest_24 = os.environ.get('API_MANIFEST_24')
api_manifest_63 = os.environ.get('API_MANIFEST_63')
api_manifest_305 = os.environ.get('API_MANIFEST_305')
api_manifest_492 = os.environ.get('API_MANIFEST_492')
api_manifest_878 = os.environ.get('API_MANIFEST_878')

#api_circles = os.environ.get('API_CIRCLES')

# response requests
response_manifest_24 = requests.get(f'{api_manifest_24}', headers=HEADER)
response_manifest_63 = requests.get(f'{api_manifest_63}', headers=HEADER)
response_manifest_305 = requests.get(f'{api_manifest_305}', headers=HEADER)
response_manifest_492 = requests.get(f'{api_manifest_492}', headers=HEADER)
response_manifest_878 = requests.get(f'{api_manifest_878}', headers=HEADER)
#response_circles = requests.get(f'{api_circles}', headers=HEADER)

# incoming json data
result_manifest_24 = response_manifest_24.json()
result_manifest_63 = response_manifest_63.json()
result_manifest_305 = response_manifest_305.json()
result_manifest_492 = response_manifest_492.json()
result_manifest_878 = response_manifest_878.json()
#result_circles = response_circles.json()

# normalize json data
df_manifest_24 = pd.json_normalize(result_manifest_24)
df_manifest_63 = pd.json_normalize(result_manifest_63)
df_manifest_305 = pd.json_normalize(result_manifest_305)
df_manifest_492 = pd.json_normalize(result_manifest_492)
df_manifest_878 = pd.json_normalize(result_manifest_878)
#df_circles = pd.json_normalize(result_circles)

print(len(df_manifest_24['circle.users'][0]))
print(len(df_manifest_63['circle.users'][0]))
print(len(df_manifest_305['circle.users'][0]))
print(len(df_manifest_492['circle.users'][0]))
print(len(df_manifest_878['circle.users'][0]))
# print(df_circles)

# for word in df_circles.columns:
#    print(df_circles[f'{word}'])

# for word in df_manifest.columns:
#    print(df_manifest[f'{word}'])

# save input as several lists, then combine into dataframe later

## -----------------------CIRCLE ID 24----------------------- ##

name_list_24 = []
address_list_24 = []
circle_id_list_24 = []
discord_username_list_24 = []
profile_address_24 = []


for dct in df_manifest_24['circle.users'][0]:
    name_list_24.append(dct['name'])
    address_list_24.append(dct['address'])
    circle_id_list_24.append(dct['circle_id'])


for dct in df_manifest_24['circle.users'][0]:
    try:
        for k, v in dct['profile'].items():
            if k == 'discord_username':
                discord_username_list_24.append(v)
            elif k == 'address':
                profile_address_24.append(v)
            else:
                print("Done.")
    except:
        AttributeError
    pass

# separate dataframe due to difference in length 613, 610
# join by eth address
len(name_list_24)
len(address_list_24)
len(circle_id_list_24)

# len = 610
len(discord_username_list_24)
len(profile_address_24)

# create dataframe from lists
df_24 = pd.DataFrame(list(zip(name_list_24, address_list_24, circle_id_list_24)),
                     columns=['Name', 'Address', 'Circle_Id'])

# add new column circle_id to df_24_a
second_circle_id_list_24 = []

for i in range(610):
    val = 24
    second_circle_id_list_24.append(val)


df_24_a = pd.DataFrame(list(zip(discord_username_list_24, profile_address_24, second_circle_id_list_24)),
                       columns=['Discord_Username', 'Profile_Address', 'Profile_Circle_Id'])

print(df_24)
print(df_24_a)

## -----------------------CIRCLE ID 63----------------------- ##

name_list_63 = []
address_list_63 = []
circle_id_list_63 = []
discord_username_list_63 = []
profile_address_63 = []


for dct in df_manifest_63['circle.users'][0]:
    name_list_63.append(dct['name'])
    address_list_63.append(dct['address'])
    circle_id_list_63.append(dct['circle_id'])


for dct in df_manifest_63['circle.users'][0]:
    try:
        for k, v in dct['profile'].items():
            if k == 'discord_username':
                discord_username_list_63.append(v)
            elif k == 'address':
                profile_address_63.append(v)
            else:
                print("Done.")
    except:
        AttributeError
    pass

# separate dataframe

# df_63
df_63 = pd.DataFrame(list(zip(name_list_63, address_list_63, circle_id_list_63)),
                     columns=['Name', 'Address', 'Circle_Id'])

# df_63_a
# add new column circle_id to df_63_a
second_circle_id_list_63 = []

for i in range(11):
    val = 63
    second_circle_id_list_63.append(val)

df_63_a = pd.DataFrame(list(zip(discord_username_list_63, profile_address_63, second_circle_id_list_63)),
                       columns=['Discord_Username', 'Profile_Address', 'Profile_Circle_Id'])

print(df_63)
print(df_63_a)

## -----------------------CIRCLE ID 305----------------------- ##


name_list_305 = []
address_list_305 = []
circle_id_list_305 = []
discord_username_list_305 = []
profile_address_305 = []


for dct in df_manifest_305['circle.users'][0]:
    name_list_305.append(dct['name'])
    address_list_305.append(dct['address'])
    circle_id_list_305.append(dct['circle_id'])


for dct in df_manifest_305['circle.users'][0]:
    try:
        for k, v in dct['profile'].items():
            if k == 'discord_username':
                discord_username_list_305.append(v)
            elif k == 'address':
                profile_address_305.append(v)
            else:
                print("Done.")
    except:
        AttributeError
    pass

# separate dataframe

# df_305
df_305 = pd.DataFrame(list(zip(name_list_305, address_list_305, circle_id_list_305)),
                      columns=['Name', 'Address', 'Circle_Id'])

# df_305_a
# add new column circle_id to df_305_a
second_circle_id_list_305 = []

for i in range(364):
    val = 305
    second_circle_id_list_305.append(val)

df_305_a = pd.DataFrame(list(zip(discord_username_list_305, profile_address_305, second_circle_id_list_305)),
                        columns=['Discord_Username', 'Profile_Address', 'Profile_Circle_Id'])

print(df_305)
print(df_305_a)

## -----------------------CIRCLE ID 492----------------------- ##

# note len = 363
name_list_492 = []
address_list_492 = []
circle_id_list_492 = []
discord_username_list_492 = []
profile_address_492 = []


for dct in df_manifest_492['circle.users'][0]:
    name_list_492.append(dct['name'])
    address_list_492.append(dct['address'])
    circle_id_list_492.append(dct['circle_id'])


for dct in df_manifest_492['circle.users'][0]:
    try:
        for k, v in dct['profile'].items():
            if k == 'discord_username':
                discord_username_list_492.append(v)
            elif k == 'address':
                profile_address_492.append(v)
            else:
                print("Done.")
    except:
        AttributeError
    pass

# separate dataframe

# df_492
df_492 = pd.DataFrame(list(zip(name_list_492, address_list_492, circle_id_list_492)),
                      columns=['Name', 'Address', 'Circle_Id'])

# df_492_a
# add new column circle_id to df_492_a
# note len = 363
second_circle_id_list_492 = []

for i in range(363):
    val = 492
    second_circle_id_list_492.append(val)

df_492_a = pd.DataFrame(list(zip(discord_username_list_492, profile_address_492, second_circle_id_list_492)),
                        columns=['Discord_Username', 'Profile_Address', 'Profile_Circle_Id'])

print(df_492)
print(df_492_a)

## -----------------------CIRCLE ID 878----------------------- ##

# note len = 373
name_list_878 = []
address_list_878 = []
circle_id_list_878 = []
discord_username_list_878 = []
profile_address_878 = []


for dct in df_manifest_878['circle.users'][0]:
    name_list_878.append(dct['name'])
    address_list_878.append(dct['address'])
    circle_id_list_878.append(dct['circle_id'])


for dct in df_manifest_878['circle.users'][0]:
    try:
        for k, v in dct['profile'].items():
            if k == 'discord_username':
                discord_username_list_878.append(v)
            elif k == 'address':
                profile_address_878.append(v)
            else:
                print("Done.")
    except:
        AttributeError
    pass

# separate dataframe

# df_878
df_878 = pd.DataFrame(list(zip(name_list_878, address_list_878, circle_id_list_878)),
                      columns=['Name', 'Address', 'Circle_Id'])

# df_878_a
# add new column circle_id to df_878_a
# note len = 373
second_circle_id_list_878 = []

for i in range(373):
    val = 878
    second_circle_id_list_878.append(val)

df_878_a = pd.DataFrame(list(zip(discord_username_list_878, profile_address_878, second_circle_id_list_878)),
                        columns=['Discord_Username', 'Profile_Address', 'Profile_Circle_Id'])

print(df_878)
print(df_878_a)

## --- CONCATENATE ALL DATAFRAMES --- ###

frames = [df_24, df_63, df_305, df_492, df_878]
frames_a = [df_24_a, df_63_a, df_305_a, df_492_a, df_878_a]

concat_frames = pd.concat(frames)
concat_frames_a = pd.concat(frames_a)

# reset index (twice) each
concat_frames_1 = concat_frames.reset_index()
concat_frames_2 = concat_frames_1.reset_index()

concat_frames_a_1 = concat_frames_a.reset_index()
concat_frames_a_2 = concat_frames_a_1.reset_index()

# select specific columns
# note: choose concat_frames_2 and concat_frames_a_2
specific_col_frames = concat_frames_2[[
    'level_0', 'Name', 'Address', 'Circle_Id']]

specific_col_frames_a = concat_frames_a_2[[
    'level_0', 'Discord_Username', 'Profile_Address', 'Profile_Circle_Id']]

# change column name 'level_0' -> 'index'
final_frames = specific_col_frames.rename(columns={'level_0': 'index'})
final_frames_a = specific_col_frames_a.rename(columns={'level_0': 'index'})

# write both files to csv
# final_frames.to_csv('coordinape_manifest_coordinape_name_address.csv')
# final_frames_a.to_csv('coordinape_manifest_coordinape_name_address_2.csv')
