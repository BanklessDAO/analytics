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
        text("SELECT id, start_date FROM bankless_snapshot_header_1 ORDER BY id DESC LIMIT 1"))
    for row in result:
        max_id = row.id
        max_start_date = row.start_date
        print("Most recent id :", max_id)
        print("Most recent start_date :", max_start_date)

# string interpolation query
variables = {'start_date': max_start_date}


query = f"""
{{
    proposals(first: 1000, skip: 0, where: {{space: "banklessvault.eth", start_gt: {max_start_date}}}) {{
        id
        title
        body
        start
        end
        state
        author
        created
        space {{
            id
            name
            members
            avatar
            __typename
        }}
        __typename
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
print('Print Most Recent Snapshot Proposal start_date  - {}'.format(result))
print('################')

# pretty print
pprint(result)

# convert list, then df
result_list = list(result.items())
lst_of_dict = result_list[0][1].get('proposals')
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
#latest_df3 = latest_df2[['index', 'id', 'title', 'start', 'end']]
# print(latest_df3)

# rename columns
# latest_df4 = latest_df3.rename(
#    columns={'index': 'id', 'id': 'proposal_id', 'start': 'start_date', 'end': 'end_date'}, inplace=False)

# print(latest_df4)
