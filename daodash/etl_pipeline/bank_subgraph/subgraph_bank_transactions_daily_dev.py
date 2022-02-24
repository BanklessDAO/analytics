# libraries for postgres connection
import os
from sqlalchemy import create_engine
from sqlalchemy import text

# http connection
import requests

# pretty print
from pprint import pprint

# context manager
import contextlib

# pandas
import pandas as pd


# using python-dotenv to access environment variables
from dotenv import load_dotenv
load_dotenv()

# NOTE: need to use environment variables to separate password from this file
# db_string = 'postgresql://user:password@localhost:port/mydatabase'

db_string = os.environ.get('DB_STRING')


@contextlib.contextmanager
def get_postgres_conn(db_string):
    """description:

    Context manager to automatically close DB connection
    Retrieve credentials from environment variables (.env)

    yield: database connection
    note: close database connection
    """

    db = create_engine(db_string)

    yield db

    db.dispose()


# use get_postgres_conn context manager
# note: interaction w/ subgraph_bank_transactions table from postgres db
with get_postgres_conn(db_string) as conn:
    result = conn.execute(
        text("SELECT MAX(tx_timestamp) AS max_tx_timestamp, MAX(id) AS max_id FROM subgraph_bank_transactions")
    )
    for row in result:
        max_tx_timestamp = row.max_tx_timestamp
        max_id = row.max_id
        print("new max_tx_timestamp: ", max_tx_timestamp)
        print("new max_id: ", max_id)

# save max_tx_timestamp externally from context manager
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


def run_query():
    """description:

    Make request to BANK subgraph api endpoint
    Use 'query' and 'variable' objects as parameters for request

    arg: 'q' or none
    return: BANK transaction data as json object 
    raise: Exception if api connection unsuccessful
    """
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


def extract_list_of_dict():
    """description:

    Extract list of dictionaries from json object 
    Each dictionary is a single BANK transaction

    arg: none
    return: list of dictionaries
    """
    result = run_query()
    result_items = result.items()
    result_list = list(result_items)
    list_of_dict = result_list[0][1].get('transferBanks')
    return list_of_dict


def transform_df():
    """description:

    Convert list_of_dict into dataframe
    Rename and reorder columns
    Important: Increment index with 'max_id' from postgres connection above
    Reset dataframe index in preparation for loading back to database

    args: none
    return: properly formatted dataframe
    """
    df = pd.json_normalize(extract_list_of_dict())

    df2 = df.rename(columns={'id': 'graph_id',
                             'timestamp': 'tx_timestamp'}, inplace=False)

    list_of_col_names = ['graph_id', 'amount_display', 'from_address',
                         'to_address', 'tx_timestamp', 'timestamp_display']
    df2 = df2.filter(list_of_col_names)
    # IMPORTANT
    df2.index += max_id
    df2 = df2.reset_index()
    df3 = df2.rename(columns={'index': 'id'}, inplace=False)
    return df3


# re-open db connection
db = create_engine(db_string)


def load_df():
    dataframe = transform_df()
    dataframe.to_sql('subgraph_bank_transactions', con=db,
                     if_exists='append', index=False)
    print("successful push, subgraph_bank_transactions table is now updated.")


# uncomment to run load_df() which pushes up backup to database
# load_df()
