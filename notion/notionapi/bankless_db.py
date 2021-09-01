import requests
import json

# DevOps Token
token = 'bankless-dao-workspace-integration-token'

# Retrieve a single database
# must add DevOps integration to each database first
# databaseId retrieved from notion url (before ?)
databaseId = 'insert-database-id'

headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2021-08-16"
}


def listAllDatabases(headers):
    readUrl = f"https://api.notion.com/v1/databases"

    res = requests.request("GET", readUrl, headers=headers)
    data = res.json()

    print(res.status_code)
    print(res.text)

    # store data in json file
    with open('./banklessdb.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


# empty results array
listAllDatabases(headers)


def retreiveDatabase(databaseId, headers):
    readUrl = f"https://api.notion.com/v1/databases/{databaseId}"

    res = requests.request("GET", readUrl, headers=headers)
    data = res.json()

    print(res.status_code)
    print(res.text)

    # store data object in json file
    # with open('./devguildprojects.json', 'w', encoding='utf8') as f:
    #    json.dump(data, f, ensure_ascii=False)


#retreiveDatabase(databaseId, headers)
