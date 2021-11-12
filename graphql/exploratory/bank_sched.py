# libraries for pipeline
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import text
import requests
import json
import pandas as pd
from pprint import pprint

# libraries for sched
import sched
import time
import logging

# Create Postgresql connection to existing table: stg_subgraph_bank_1
# NOTE: need to use environment variables to separate password from this file
# db_string = 'postgresql://user:password@localhost:port/mydatabase'

db_string = 'postgresql://user:password@localhost:port/mydatabase'
db = create_engine(db_string)

# IMPORTANT: grab max_id to later reset_index() to properly append updated dataframe into existing table on primary key (id)
with db.connect() as conn:
    result = conn.execute(
        text("SELECT MAX(tx_timestamp) AS max_tx_timestamp, MAX(id) AS max_id FROM stg_subgraph_bank_1"))
    for row in result:
        max_tx_timestamp = row.max_tx_timestamp
        max_id = row.max_id
        print("new max_tx_timestamp: ", max_tx_timestamp)
        print("new max_id: ", max_id)

variables = {'input': max_tx_timestamp}

# BANK Subgraph GraphQL query
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

# Run Query to BANK Subgraph


def run_query(q):
    request = requests.post('https://api.studio.thegraph.com/query/1121/bankv1/v0.0.5'
                            '',
                            json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query))


# pretty print
print('################')
pprint(result)


def graph_etl(query):
    # exec run_query and save to results
    result = run_query(query)
    # Convert result from JSON to pandas dataframe
    result_items = result.items()
    result_list = list(result_items)
    lst_of_dict = result_list[0][1].get('transferBanks')
    df = pd.json_normalize(lst_of_dict)
    # Change column names from dataframe to match Table in PostgreSQL
    df2 = df.rename(columns={'id': 'graph_id',
                             'timestamp': 'tx_timestamp'}, inplace=False)
    # Reorder columns using list of names
    list_of_col_names = ['graph_id', 'amount_display', 'from_address',
                         'to_address', 'tx_timestamp', 'timestamp_display']
    df2 = df2.filter(list_of_col_names)
    # IMPORTANT
    # increment index with max_id (see postgresql connection above)
    df2.index += max_id
    df2 = df2.reset_index()
    df3 = df2.rename(columns={'index': 'id'}, inplace=False)
    print(df3)
    print("#### need to un-comment next line to push to postgres ####")
    #df3.to_sql('stg_subgraph_bank_1', con=db, if_exists='append', index=False)
    return df3


# To print out timestamps for 'first priority' and 'positional'
def print_time(a='default'):
    print("From print_time", time.time(), a)


def schedule_etl(query):
    print("First Timestamp: ", time.time())
    graph_etl(query)
    event_schedule.enter(40, 2, print_time, argument=('second in queue',))
    event_schedule.enter(25, 1, print_time, kwargs={'a': 'first in queue'})
    event_schedule.run()
    #event_schedule.enter(50, 3, schedule_etl(query),)
    print("Last Timestamp: ", time.time())


event_schedule = sched.scheduler(time.time, time.sleep)
print("Initiate schedule_etl...\n")
event_schedule.enter(50, 3, schedule_etl(query),)
print("\n Closing schedule_etl...")
