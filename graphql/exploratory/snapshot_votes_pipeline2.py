import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

import requests
import json
import pandas as pd
from pprint import pprint

# establish postgres connection for DAO Dash
# SELECT proposal_id FROM bankless_snapshot_header_1 ORDER BY id DESC LIMIT 1
# save proposal_id as variables
# query GraphQL endpoint for snapshot_votes, insert proposal_id
# run query, convert json outout to dataframe

# db_string = 'postgresql://user:password@localhost:port/mydatabase'
db_string = 'postgresql://dao_dash_app:W6BlwLwv2foA1AvR@db-postgresql-nyc3-31688-do-user-9472067-0.b.db.ondigitalocean.com:25060/dao_dash'
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

variables = {'created': max_created}

query2 = f"""
{{
        votes(first: 10000, where: {{created: {max_created}}}) {{
          id
          voter
          created
          choice
          __typename
          proposal {
            id
          }
        }}
}}
"""

def run_query(q):
    request = requests.post('https://hub.snapshot.org/graphql'
                            '',
                            json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query))


result = run_query(query)

# print results
print('Print Most Recent Snapshot Votes ID Result - {}'.format(result))
print('################')

# pretty print
pprint(result)