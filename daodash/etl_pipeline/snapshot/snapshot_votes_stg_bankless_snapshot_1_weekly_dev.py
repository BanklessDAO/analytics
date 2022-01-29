# libraries for pipeline
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

# Create Postgresql connection to existing table: stg_bankless_snapshot_1
# NOTE: need to use environment variables to separate password from this file
# db_string = 'postgresql://user:password@localhost:port/mydatabase'

db_string = os.environ.get('DB_STRING')
db = create_engine(db_string)

def get_db_max():
    ## initalize variables
    max_id = 0
    max_created = 0

    # IMPORTANT: grab max_id to later reset_index() to properly append updated dataframe into existing table on primary key (id)
    # also grab max_created
    with db.connect() as conn:
        result = conn.execute(
            text("SELECT id, created FROM stg_bankless_snapshot_1 ORDER BY id DESC LIMIT 1"))
        for row in result:
            max_id = row.id
            max_created = row.created
            print("Most recent id :", max_id)
            print("Most recent created :", max_created)
    
    return {
        "max_id": max_id,
        "max_created": max_created
    }

def get_snapshot_query(maxes):
    max_id = maxes["max_id"]
    max_created = maxes["max_created"]
    # String interpolation query2 works
    # note: {{ }} required for all non-variables, see proposal.id
    # need to add '_gt' for greater than previous timestamp
    return f"""
    {{
        votes(first: 1000, where: {{created_gt: {max_created}, space: "banklessvault.eth"}}, orderBy:"created", orderDirection:asc) {{
        id
        voter
        created
        choice
        vp
        vp_by_strategy
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

# Run query to Snapshot Votes API endpoint
# returns request as json

def run_snapshot_query(query, maxes):
    variables = {'created': maxes["max_created"]}
    request = requests.post('https://hub.snapshot.org/graphql'
                            '',
                            json={'query': query, 'variables': variables})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query))


# pretty print
# print('Print Most Recent Snapshot Votes ID Result - {}'.format(result))
# print('################')
# pprint(result)


def parse_save_results(result, maxes):    
    # convert results from JSON to pandas
    result_items = result.items()
    result_list = list(result_items)
    lst_of_dict = result_list[0][1].get('votes')
    df = pd.json_normalize(lst_of_dict)
    # reset index
    # note: indexing in python starts with 0
    df.index += 1
    df.index += maxes["max_id"]
    df2 = df.reset_index()
    # print(vars(df2[['voter']]))
    # select specific columns
    df3 = df2[['index', 'id', 'voter', 'created', 'choice', '__typename', 'proposal.id', 'vp']]
    # change column name
    df4 = df3.rename(
        columns={'index': 'id', 'id': 'vote_id', 'proposal.id': 'proposal_id', 'vp':'bank_voting'}, inplace=False)
    # print(df4)
    # print("#### need to un-comment next line to push to postgres ####")
    df4.to_sql('stg_bankless_snapshot_1', con=db, if_exists='append', index=False)
    return df4

def has_votes(json):
    return json != {'data': {'votes': []}}


def snapshot_votes_etl():
    maxes = get_db_max()
    query = get_snapshot_query(maxes)
    json_result = run_snapshot_query(query, maxes)
    if has_votes(json_result):
        parse_save_results(json_result, maxes)
        return "continue"
    else:
        return "halt"

while snapshot_votes_etl() != "halt":
    print("...")