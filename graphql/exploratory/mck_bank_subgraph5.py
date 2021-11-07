
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

import requests
import json
import pandas as pd
from pprint import pprint

# db_string = 'postgresql://user:password@localhost:port/mydatabase'
# change password

db_string = 'postgresql://user:password@localhost:port/mydatabase'

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
        text("SELECT MAX(tx_timestamp) AS max_tx_timestamp, MAX(id) AS max_id FROM stg_subgraph_bank_1"))
    for row in result:
        max_tx_timestamp = row.max_tx_timestamp
        max_id = row.max_id
        print("new max_tx_timestamp: ", max_tx_timestamp)
        print("new max_id: ", max_id)


# Run separate request to GraphQL endpoint
# use max_tx_timestamp in parameter 'where: {timestamp_gte: max_tx_timestamp}'
# this will return on-chain tx since latest timestamp (i.e., max_tx_timestamp)

variables = {'input': max_tx_timestamp}

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

# note: 'variables' defined above


def run_query(q):
    request = requests.post('https://api.studio.thegraph.com/query/1121/bankv1/v0.0.5'
                            '',
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

result_items = result.items()
result_list = list(result_items)
lst_of_dict = result_list[0][1].get('transferBanks')
df = pd.json_normalize(lst_of_dict)

# df = df.reset_index()  # reset index to later increment with max_id
# df.index += max_id  # increment with max_id
print(df)

# TEST CREATE: write results from df into *new* stg_subgraph_bank_test through 'db' connection established above
# if_exists parameter for existing table
# df.to_sql('stg_subgraph_bank_test', db, if_exists='append')
#print('Test: df written to stg_subgraph_bank_test')

# TEST INSERT: check status of stg_subgraph_bank_test, then insert to *that* table first
# check latest timestamp/timestamp_display in postgres (stg_subgraph_bank_test)          1636166865, Sat, 06 Nov 2021 02:47:45 GMT
# check latest timestamp/timestamp_display when query in python (stg_subgraph_bank_test) 1636187698, Sat, 06 Nov 2021 08:34:58 GMT
# can TEST INSERT on stg_subgraph_bank_test

# expect to get ~ 412 rows
# check stg_subgraph_bank_test -- append = 402 + 412 = 814 (not what we want)
# df.to_sql('stg_subgraph_bank_test', db, if_exists='append')
# print number of rows in dataframe
print("Number of rows in df: ", len(df.index))

# TEST INSERT:

# NOTE: need to change data frame columns to match stg_subgraph_bank
# - run: connecting timestamp 1635654941
#       SELECT * FROM stg_subgraph_bank
#       LIMIT ALL OFFSET 19950

# - sync with last row on stg_subgraph_bank_test

# change column name
# id, graph_id, amount_display, from_address, to_address, tx_timestamp, timestamp_display

# print current columns
print(df.columns)

# use rename function, set inplace=False to preserve original dataframe column name
df2 = df.rename(columns={'id': 'graph_id',
                         'timestamp': 'tx_timestamp'}, inplace=False)

print(df2)

# reorder dataframe column using list of names
# list of names (in same order as stg_subgraph_bank)
list_of_col_names = ['graph_id', 'amount_display', 'from_address',
                     'to_address', 'tx_timestamp', 'timestamp_display']
df2 = df2.filter(list_of_col_names)
df2.index += max_id  # increment with max_id
df2 = df2.reset_index()  # reset index to later increment with max_id

df3 = df2.rename(columns={'index': 'id'}, inplace=False)

print(df3)
# Then insert pandas df to postgres table, note primary key

df3.to_sql('stg_subgraph_bank_1', con=db, if_exists='append', index=False)

print("Done. Check pgAdmin")


# write results from df into stg_subgraph_bank in Postgres using INSERT INTO syntax with sqlalchemy
# see pgAdmin script

# INSERT INTO public.stg_subgraph_bank() VALUES ();
