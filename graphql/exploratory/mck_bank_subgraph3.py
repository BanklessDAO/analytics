import requests
import json
import pandas as pd


from pprint import pprint

# Use Pagination in GraphQL query


def run_query(q):
    # using McKethanor Bank Subgraph Queries (HTTP)
    # end point to make request
    # https://api.studio.thegraph.com/query/1121/bankv1/v0.0.5  -- McKethanor api
    # should not need to replace [api-key] as this is self-hosted instead of deployed subgraph ?
    # should not need to deposit GRT in billing
    # before query
    request = requests.post('https://api.studio.thegraph.com/query/1121/bankv1/v0.0.5'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query))


# use Pagination with after: $timestamp
# timestamp "1620159318" = May 5, 2021
# timestamp "1620517404" = May 8, 2021
query = """
{
    transferBanks(first: 1000, skip: 5000, after: {timestamp: "1620517404"}, orderBy: timestamp, orderDirection: asc, subgraphError: allow) {
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

# print results
print('Print Bank Subgraph Result - {}'.format(result))
print('################')

# pretty print
pprint(result)

# convert to list
# then dig down nested layers

result_items = result.items()
result_list = list(result_items)
lst_of_dict = result_list[0][1].get('transferBanks')
df = pd.json_normalize(lst_of_dict)

print(df)
