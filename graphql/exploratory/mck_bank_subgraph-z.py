
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

import requests
import json
import pandas as pd
from pprint import pprint

# db_string = 'postgresql://user:password@localhost:port/mydatabase'
# change password
db_string = 'postgresql://postgres:postgres@localhost/bankless'

db = create_engine(db_string)

########################

# Create TEST table to confirm connection

# db.execute(
#    "CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")

# db.execute(
#    "INSERT INTO films (title, director, year) VALUES ('Dune', 'Denis Villeneuve', '2021')")

# Read
#result_set = db.execute("SELECT * FROM films")
# for r in result_set:
#    print(r)

########################


# Query existing postgres table: stg_subgraph_bank
# read from stg_subgraph_bank to get MAX (tx_timestamp)
# set to variable max_tx_timestamp

with db.connect() as conn:
    result = conn.execute(
        text("SELECT MAX(tx_timestamp) AS max_tx_timestamp FROM stg_subgraph_bank"))
    for row in result:
        max_tx_timestamp = row.max_tx_timestamp
        print("new max_tx_timestamp: ", max_tx_timestamp)


# Run separate request to GraphQL endpoint
# use max_tx_timestamp in parameter 'where: {timestamp_gte: max_tx_timestamp}'
# this will return on-chain tx since latest timestamp (i.e., max_tx_timestamp)


query = f"""
{{
  transferBanks(first: 1000, where: {{timestamp_gte:{max_tx_timestamp}}}, orderBy: timestamp, orderDirection: asc, subgraphError: allow) {{
    id
    from_address
    to_address
    amount
    amount_display
    timestamp
    timestamp_display
  }}
}}
"""

print(query)

variables = {'input': max_tx_timestamp}


def run_query(q):
    request = requests.post('https://api.studio.thegraph.com/query/1121/bankv1/v0.0.5',
                            json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query))


result = run_query(query)

# print results
print('Print Bank Subgraph Result - {}'.format(result))
print('################')

# pretty print
pprint(result)


# write results from graphql json to pandas df
# write results from df into stg_subgraph_bank in Postgres using INSERT INTO syntax with sqlalchemy
# see pgAdmin script

# INSERT INTO public.stg_subgraph_bank() VALUES ();