# libraries for mongodb connection
import os
from sqlite3 import dbapi2
import pymongo
from pymongo import MongoClient

# context manager
# import contextlib

# pandas
from pandas import DataFrame

# pretty print
from pprint import pprint

# using python-dotenv to access environment variables
from dotenv import load_dotenv
load_dotenv()

# NOTE: need to use environment variables to separate password from this file
# connection_string = 'mongodb+srv://user:password@cluster0.iojup.mongodb.net/database_name'

connection_string = os.environ.get('CONNECTION_STRING')
client = MongoClient(connection_string)

# client is a dictionary of databases
db = client['bountyboard']

# collections are attributes of databases
bounties_col = db['bounties']

# print first document in bounties collection
# print(bounties_col.find_one())


# count documents in bounties collection
filter = {}
n_bounties = bounties_col.count_documents(filter)
print(n_bounties)

# find one document to inspect
first_bounties_doc = bounties_col.find_one(filter)
pprint(first_bounties_doc)

# get the fields present in the *first* document
# note: document schema changes later on
print(list(first_bounties_doc.keys()))

# find latest document to inspect
latest_bounties_doc = bounties_col.find().skip(n_bounties - 1)
pprint(list(latest_bounties_doc)[0])

# print only keys
# print(list(latest_bounties_doc)[0].keys())


# composing filters
# filter for customer_id
# filter for customerId

customer_id_filter = {'customer_id': '834499078434979890'}

customerId_filter = {'customerId': '834499078434979890'}

print("Number of Bankless bounties with customer_id: ",
      bounties_col.count_documents(customer_id_filter))
print("Number of Bankless bounties with customerId: ",
      bounties_col.count_documents(customerId_filter))

print("First bounty that introduced customerId: ",
      bounties_col.find_one(customerId_filter))

# Cross-Check: count_documents after createdAt: '2021-12-09' and customerId: '834499078434979890'
# n = 67
bounties_col.count_documents({
    'customerId': '834499078434979890',
    'createdAt': {'$gte': '2021-12-09'}
})

# ----- Cross-check: 219% growth after Jan 1st ------#
# Cross-Check: count_documents after createdAt: '2021-12-09' and before '2022-01-01' and customerId: '834499078434979890'
# n = 21
# calculation: 67 - 21 = 46 || 4600/21 = 219%
bounties_col.count_documents({
    'customerId': '834499078434979890',
    'createdAt': {'$gte': '2021-12-09', '$lt': '2022-01-01'}
})

# ---- load bounties_col into dataframe ----- #
# n = 67 (rows)
df = DataFrame(list(bounties_col.find({'customerId': '834499078434979890'})))
print(df)
