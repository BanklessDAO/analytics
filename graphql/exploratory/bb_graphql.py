import requests
import json
import pandas as pd

from pprint import pprint


def run_query(q):
    request = requests.post('http://localhost:3333/api/graphql'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query))


# basic query first
query = """

{
    Bounties(field: "rewardAmount", greaterThan: 1000) {
    id
    title
    season
    description
    rewardAmount
  }
}
"""

result = run_query(query)

# print results
print('Print Bounties Result - {}'.format(result))
print('################')

# pretty print
pprint(result)
