import requests
import json

# Resource Integration Token
token = 'my-integrations-token'

databaseId = '9f9164dfad6142318d72c8f837e51317'

headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2021-08-16"
}


def readDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", readUrl, headers=headers)
    data = res.json()
    print(res.status_code)
    print(res.text)

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


def createPage():
    pass


def updatePage():
    pass


readDatabase(databaseId, headers)
