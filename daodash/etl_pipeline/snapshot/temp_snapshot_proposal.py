# libraries for pipeline
import os
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


# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

# Create Postgresql connection to existing table: stg_bankless_snapshot_1
# NOTE: need to use environment variables to separate password from this file
# db_string = 'postgresql://user:password@localhost:port/mydatabase'


db_string = os.environ.get('DB_STRING')
db = create_engine(db_string)

with db.connect() as conn:
    result = conn.execute(
        # note ORDER BY start_date, not id
        text("SELECT id, start_date FROM bankless_snapshot_header_1 ORDER BY start_date DESC LIMIT 1"))
    for row in result:
        max_id = row.id
        max_start_date = row.start_date
        print("Most recent id :", max_id)
        print("Most recent start_date :", max_start_date)

# string interpolation query
variables = {'start_date': max_start_date}

# NOTE: if postgres table is already up to date, 'start_gt' will return an empty dataframe
# change 'start_gt' to 'start' to test this endpoint
query = f"""
{{
    proposals(first: 1000, skip: 0, where: {{space: "banklessvault.eth"}}) {{
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

# Run query to Snapshot Votes API endpoint
# returns request as json


def run_query(q):
    request = requests.post('https://hub.snapshot.org/graphql'
                            '',
                            json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query))


# pretty print
print('Print Most Recent Snapshot Proposals - {}'.format(result))
print('################')
pprint(result)


def snapshot_proposal_etl(query):
    # execute run_query and save to result
    result = run_query(query)
    # convert results from JSON to pandas
    result_list = list(result.items())
    lst_of_dict = result_list[0][1].get('proposals')
    df = pd.json_normalize(lst_of_dict)
    # reset index
    # note: indexing in python starts with 0
    print("PRINT df: ", df)
    #df.index += 1
    #df.index += max_id
    #df2 = df.sort_index(ascending=False)
    df2 = df.sort_index(ascending=False).reset_index()
    print(df2)
    # select specific columns
    # df3 = df2[['index', 'id', 'title', 'start', 'end']]
    df3 = df2.reset_index()
    df4 = df3[['level_0', 'id', 'title', 'start', 'end']]
    print(df4)
    df5 = df4.rename(columns={
                     'level_0': 'id', 'id': 'proposal_id', 'start': 'start_date', 'end': 'end_date'})
    print(df5)
    # change column name
    #df4 = df3.rename(columns={'level_0': 'id', 'id': 'proposal_id', 'start': 'start_date', 'end': 'end_date'}, inplace=False)
    # print(df4)
    print("#### need to un-comment next line to push to postgres ####")
    # df5.to_sql('bankless_snapshot_header_2', con=db, if_exists='append', index=False)
    return df5


# To print out timestamps for 'first priority' and 'positional'
snapshot_proposal_etl(query)
