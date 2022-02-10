import os
from dotenv import load_dotenv  # for python-dotenv method
load_dotenv()  # for python-dotenv method


def get_database():
    """Description

    establish connection to mongo client and return

    Args: none.

    Return: client connection
    Notes/Raises:
    """
    from pymongo import MongoClient
    import pymongo
    connection_string = os.environ.get('CONNECTION_STRING')
    client = MongoClient(connection_string)
    return client


def get_collection():
    """Description:

    Go through bountyboard database and bounties collection

    Args: none.

    Return: all bounties
    Notes/Raises:
    """
    dbname = get_database()
    bb = dbname['bountyboard']
    col = bb['bounties']
    return col


results = list(get_collection().find())
print(type(results))

# if __name__ == "__main__":
#    dbname = get_database()
#    print(dbname)
