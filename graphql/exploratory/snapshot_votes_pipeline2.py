import os
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

import requests
import json
import pandas as pd
from pprint import pprint

# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()


db_string = os.environ.get('DB_STRING')
db = create_engine(db_string)

with db.connect() as conn:
    result = conn.execute(
        text("SELECT id, created FROM stg_bankless_snapshot_1 ORDER BY id DESC LIMIT 1"))
    for row in result:
        max_id = row.id
        max_created = row.created
        print("Most recent id :", max_id)
        print("Most recent created :", max_created)

# Hard coded version: works

query = """
{
        votes(first: 10000, where: {created: 1635966410}) {
          id
          voter
          created
          choice
          __typename
          proposal {
            id
          }
        }
}
"""

# String interpolation not working

variables = {'created': max_created}
query2 = f"""
{{
        votes(first: 10000, where: {{created: {max_created}}}) {{
          id
          voter
          created
          choice
          __typename
          proposal {{
            id
          }}
        }}
}}
"""

# Second String interpolation attempt
# note: f""" yield an error

query3 = """
mutation createVote {
  createVote(input: {
      id: "0x0cfb9c3476157243303e1e5cef02e7719b261b566c377a1e23586915e8f604b3", 
      voter: "0x4f8c2d5397262653Cd8956CB977A0bA3660210c7", 
      created: "1635966410", 
      __typename: "Vote", 
      proposal: {"id": "0xabccf8394b35e92043a4055f8430f1babd44fdc763849ad0158441073578a62e"}
      }) {
    votes {
        id
        voter
        created
        __typename
        proposal {
            id
        }
    }
  }
}
"""

# Third string interpolation attempt
# note: f""" yield an error

# variables = {
#    "input": {
#        "id": "0x0cfb9c3476157243303e1e5cef02e7719b261b566c377a1e23586915e8f604b3",
#        "voter": "0x4f8c2d5397262653Cd8956CB977A0bA3660210c7",
#        "created": "1635966410",
#        "__typename": "Vote",
#        "proposal": {"id": "0xabccf8394b35e92043a4055f8430f1babd44fdc763849ad0158441073578a62e"}
#    }
# }


query4 = """
mutation createUser($input: CreateUserInput!) {
  createUser(input: $input) {
    user {
      id
      voter
      created
      __typename
      proposal {
            id
      }
    }
  }
}
"""


def run_query(q):
    request = requests.post('https://hub.snapshot.org/graphql'
                            '',
                            json={'query': query2, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query2))


result = run_query(query2)

# print results
print('Print Most Recent Snapshot Votes ID Result - {}'.format(result))
print('################')

# pretty print
pprint(result)
