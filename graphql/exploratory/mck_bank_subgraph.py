import requests
import json
import pandas as pd

from pprint import pprint

# function to use requests.posts to make API call to subgraph url


def run_query(q):
    # using McKethanor Bank Subgraph Queries (HTTP)
    # end point to make request
    # https://api.studio.thegraph.com/query/1121/bankv1/v0.0.5  -- McKethanor api
    # should not need to replace [api-key] as this is self-hosted instead of deployed subgraph ?
    # should not need to deposit GRT in billing
    # before query
    # NOTE 'query2'
    request = requests.post('https://api.studio.thegraph.com/query/1121/bankv1/v0.0.5'
                            '',
                            json={'query': query2})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query2))

# The Graph Query
# PAGINATION:

# basic query first


query = """

{
    transferBanks(first: 1000, orderBy: timestamp, orderDirection: asc, subgraphError: allow) {
    id
    from_address
    to_address
    amount
    amount_display
    timestamp
    timestamp_display
  }
}
"""

query2 = """

{
    transferBanks(first: 1000, where: {timestamp_gte: "1620159318"}, orderBy: timestamp, orderDirection: asc, subgraphError: allow) {
    id
    from_address
    to_address
    amount
    amount_display
    timestamp
    timestamp_display
  }
}
"""

result = run_query(query)
result2 = run_query(query2)

# print results
print('Print Bank Subgraph Result - {}'.format(result))
print('################')

# pretty print
pprint(result)

# convert to list
# then dig down nested layers

#result_items = result.items()
#result_list = list(result_items)

#lst_of_dict = result_list[0][1].get('transferBanks')

#df = pd.json_normalize(lst_of_dict)

# print(df)


# repeat beyond {timestamp_gte:"1620159318"}

result_items_2 = result2.items()
result_list_2 = list(result_items_2)

lst_of_dict_2 = result_list_2[0][1].get('transferBanks')

df2 = pd.json_normalize(lst_of_dict_2)

print(df2)
