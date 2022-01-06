import os
import requests
from pydiscourse import DiscourseClient
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()


client = DiscourseClient(
    'https://forum.bankless.community',
    api_username='paulapivat',
    api_key=os.environ.get('API_STRING')
)

# get user
user = client.user('paulapivat')
pprint(user)

# print user topics
user_topics = client.topics_by('paulapivat')

# loop through user_topics list
# grab key from each dict
# 'fancy_title'

for dct in user_topics:
    for key, value in dct.items():
        if key == 'fancy_title':
            print(value)
        else:
            pass
