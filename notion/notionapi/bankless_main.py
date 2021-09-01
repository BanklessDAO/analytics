import requests
import json

# DevOps Token
token = 'bankless-dao-workspace-integration-token'

# Retrieve Single User
# run listAllUsers first to get single userId
userId = 'single-userId'

headers = {
    "Authorization": "Bearer " + token,
    "Notion-Version": "2021-08-16"
}


def listAllUsers(headers):
    readUrl = f"https://api.notion.com/v1/users"

    res = requests.request("GET", readUrl, headers=headers)
    data = res.json()

    print(res.status_code)
    print(res.text)

    # will create json file
    with open('./listusers.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False)


listAllUsers(headers)


def retrieveOneUser(userId, headers):
    readUrl = f"https://api.notion.com/v1/users/{userId}"

    res = requests.request("GET", readUrl, headers=headers)
    data = res.json()

    print(res.status_code)
    print(res.text)


retrieveOneUser(userId, headers)
