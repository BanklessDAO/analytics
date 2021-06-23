# reference: http://cryptomarketpool.com/use-the-graph-to-query-ethereum-data-in-python/

import requests
# print out put in easy to read format (necessary for printing long nested dictionaries)
from pprint import pprint

# function to use requests.post to make API call to subgraph url


def run_query(q):
    # endpoint to make request
    request = requests.post('https://api.thegraph.com/subgraphs/name/poap-xyz/poap-xdai'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query))


# The Graph query - Query poap.xDai event where {id: 2655}
# PAGINATION: specify, tokens(first: 200) to reconcile with CSV total 173
# add tokensOwned ~ Power (poap.gallery)

query = """

{
  events(where: { id: 2655 }) {
    id
    tokens(first: 200) {
      id
      owner {
        id
        tokensOwned
      }
      transfers {
        id
        timestamp
        from {
          id
        }
        to {
          id
        }
      }
    }
  }
}
"""

result = run_query(query)

# print results
print('Print Result - {}'.format(result))
print('##############')
# pretty print - printing long nested dictionaries
pprint(result)

# ensure event id is 2655
# reconcile with poap.gallery,
# Bankless DAO Community Call #4, event id 2655
# csv with 173 rows (previous downloaded raw csv had 172), late claimer on June 11th, 2021

# ensure event queried is id #2655
result['data']['events'][0]['id']

# list of all tokens for event id #2566
result['data']['events'][0]['tokens']

# tokens should be a list of dictionaries
type(result['data']['events'][0]['tokens'])      # list
type(result['data']['events'][0]['tokens'][0])   # dict

# check length of list -- ideally, should match 173 rows
# however only get 100 (need to reconcile why)
# CONCLUSION: in above query need to specify token(first: 200) to query more than 100 results (pagination)
len(result['data']['events'][0]['tokens'])
