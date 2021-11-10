
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text

import requests
import json
import pandas as pd
from pprint import pprint

# Create connection Postgresql connection
# db_string = 'postgresql://user:password@localhost:port/mydatabase'
# NOTE: need to use environment variables to separate password from this file

db_string = 'postgresql://user:password@localhost:port/mydatabase'
db = create_engine(db_string)

# NOTE: If first time, create a test table and insert data to ensure a connection to postgres is working.

# Query stg_subgraph_bank_1 (from postgresql db)
# read from stg_subgraph_bank_1 to get MAX (tx_timestamp)
# set to variable max_tx_timestamp
# IMPORTANT: grab max_id to later reset_index() to properly append updated dataframe into existing table on primary key (id)

with db.connect() as conn:
    result = conn.execute(
        text("SELECT MAX(tx_timestamp) AS max_tx_timestamp, MAX(id) AS max_id FROM stg_subgraph_bank_1"))
    for row in result:
        max_tx_timestamp = row.max_tx_timestamp
        max_id = row.max_id
        print("new max_tx_timestamp: ", max_tx_timestamp)
        print("new max_id: ", max_id)


# Run separate request to GraphQL endpoint
# use python f-string for interpolation into 'where: {{timestamp_gte: {max_tx_timestamp}}}'
# this will return on-chain tx since latest timestamp (i.e., max_tx_timestamp)
# set variable as object max_tx_timestamp as value


variables = {'input': max_tx_timestamp}

# note: timestamp_gt instead of timestamp_gte ('e', 'or equal to' duplicates rows)
query = f"""
{{
  transferBanks(first: 1000, where: {{timestamp_gt:{max_tx_timestamp}}}, orderBy: timestamp, orderDirection: asc, subgraphError: allow) {{
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

# Run


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


# Convert 'result' from JSON to pandas dataframe
# turn to list of dictionaries, then dataframe

result_items = result.items()
result_list = list(result_items)
lst_of_dict = result_list[0][1].get('transferBanks')
df = pd.json_normalize(lst_of_dict)

print(df)
print("Number of rows in df: ", len(df.index))
print(df.columns)

# Change column names from dataframe to match Table in PostgreSQL
# Use rename() function, set inplace=False to preserve original dataframe column name
# save as new dataframe (df2)
df2 = df.rename(columns={'id': 'graph_id',
                         'timestamp': 'tx_timestamp'}, inplace=False)

print(df2)

# Reorder column using list of names
# list of names (in same order as stg_subgraph_bank_1)
list_of_col_names = ['graph_id', 'amount_display', 'from_address',
                     'to_address', 'tx_timestamp', 'timestamp_display']
df2 = df2.filter(list_of_col_names)

# IMPORTANT
# increment index with max_id (see postgresql connection above)
# use reset_index() to create new column with incremented index
# NOTE: needed to append to existing table stg_subgraph_bank_1 without messing up the table
# (1 row is duplicated)
df2.index += max_id
df2 = df2.reset_index()

# rename column from index to id to match stg_subgraph_bank_1
df3 = df2.rename(columns={'index': 'id'}, inplace=False)
print(df3)

# INSERT dataframe to postgres table using to_sql() function from sqlalchemy
# NOTE: if_exists='append' and index=false
# NOTE: Comment out this section to prevent writing to database

#df3.to_sql('stg_subgraph_bank_1', con=db, if_exists='append', index=False)
#print("Done. Check pgAdmin")
