# libraries for postgres connection
import os
from webbrowser import get
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

    Automatically close DB connection
    Retrieve credentials from environment variables (.env)

    yield: database connection
    note: close database connection after function call
    """

    db = create_engine(db_string)

    yield db

    db.dispose()


# query subgraph_bank_transactions table from postgres db

# this query of the 'id' column shows there are duplicates
with get_postgres_conn(db_string) as conn:
    result = conn.execute(
        text("SELECT id, COUNT(id) FROM subgraph_bank_transactions GROUP BY id HAVING COUNT(id) > 1 LIMIT 10")
    )
    n = 0
    for row in result:
        n += 1
        print("row :", row)
        if n > 0:
            print("There are duplicates.")
            break
        else:
            print("No duplicates!")

# this query of the 'graph_id' column shows there are *no* duplicates
with get_postgres_conn(db_string) as conn:
    result = conn.execute(
        text("SELECT graph_id, COUNT(graph_id) FROM subgraph_bank_transactions GROUP BY graph_id HAVING COUNT(graph_id) > 1 LIMIT 10")
    )
    n = 0
    for row in result:
        n += 1
        print("row :", row)
        if n > 0:
            print("There are duplicates.")
            break
        else:
            print("No duplicates!")


# incorporating vw_dupe_check_script
with get_postgres_conn(db_string) as conn:
    result = conn.execute(
        text("SELECT * FROM vw_dupe_check_script")
    )
    for row in result:
        print("vw_dupe_check_script :", row)
