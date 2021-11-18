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

# String interpolation query2 works
# note: {{ }} required for all non-variables, see proposal.id

variables = {'created': max_created}
query2 = f"""
{{
        votes(first: 10000, where: {{created_gt: {max_created}, space: "banklessvault.eth"}}) {{
          id
          voter
          created
          choice
          __typename
          proposal {{
            id
            space {{
              id
            }}
          }}
        }}
}}
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

# convert list, then df
result_list = list(result.items())
lst_of_dict = result_list[0][1].get('votes')
latest_df = pd.json_normalize(lst_of_dict)

pprint(latest_df)

# update index
# add max_id
# reset_index
latest_df.index += 1   # because indexing in python starts with 0
latest_df.index += max_id
latest_df2 = latest_df.reset_index()
print(latest_df2)

# select specific columns
latest_df3 = latest_df2[['index', 'id', 'voter',
                         'created', 'choice', '__typename', 'proposal.id']]

print(latest_df3)
# rename columns

# change column names index = id, id = vote_id, proposal.id = proposal_id
latest_df4 = latest_df3.rename(
    columns={'index': 'id', 'id': 'vote_id', 'proposal.id': 'proposal_id'}, inplace=False)

print(latest_df4)

# push back up to postgres
