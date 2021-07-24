import requests
import json


def retrieve_messages(channel_id):
    num = 0
    headers = {
        'authorization': 'code'
    }
    r = requests.get(
        f'https://discordapp.com/api/channels/{channel_id}/messages?limit=100', headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(value, '\n')
        num = num+1
    print('number of messages collected is', num)


retrieve_messages('channel_id')
print('done.')
