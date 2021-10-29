import requests
import json
import pandas as pd

from pprint import pprint

# function to use requests.posts to make API call to subgraph url


def run_query(q):
    # using 0xNSHuman Bank Subgraph Queries (HTTP)
    # end point to make request
    # https://api.thegraph.com/subgraphs/name/0xnshuman/bank-subgraph
    # https://api.studio.thegraph.com/query/1121/bankv1/v0.0.5  -- McKethanor api
    # should not need to replace [api-key] as this is self-hosted instead of deployed subgraph ?
    # should not need to deposit GRT in billing
    # before query
    request = requests.post('https://api.thegraph.com/subgraphs/name/0xnshuman/bank-subgraph'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query))

# The Graph Query
# PAGINATION:

# basic query first
# see Art Blocks in The Graph "Playground" for query explanations
# source: https://thegraph.com/explorersubgraph?id=0x0a0319671f2d3c18fb55ab555b48bc01f27747a4-0&view=Playground


query = """

{
    accounts(first: 5) {
    id
    asERC20 {
      id
    }
    ERC20balances {
      id
    }
    ERC20approvalsOwner {
      id
    }
  }
}
"""

result = run_query(query)

# print results
print('Print Bank Subgraph Result - {}'.format(result))
print('################')

# pretty print
pprint(result)

# convert to dataframe
# challenge: dictionary is nested, so we need to flatten first
result_items = result.items()
# note: result_list is a list that contains a tuple of length 2
# result_list[0][0] = 'data'
result_list = list(result_items)

# dataframe (column 1 needs flattening)
df = pd.DataFrame(result_list)


# steps to flatten nested dictionary

# define data type in layers

# type(result) = dict
# type(result_items) = dict_items
# type(result_list) = list
# type(result_list[0]) = tuple
# type(result_list[0][0]) = str
# type(result_list[0][1]) = dict

# define number of layers

# len(result_list) = 1      list contains one tuple
# len(result_list[0]) = 2   tuple contains two items; first item 'str', second item 'dict'
# len(result_list[0][1]) = 1

# tease apart dict by key & value
# grab value in the dict using .get() method

# type(result_list[0][1].get('accounts')) = list
# len(result_list[0][1].get('accounts')) = 5 ; list with 5 (dict)
# type(result_list[0][1].get('accounts')[0]) = list

for lst in result_list[0][1].get('accounts'):
    print(lst, "\n")

# retry conversion to dataframe now that we are at base layer
# convert list of dictionaries to dataframe
lst_of_dict = result_list[0][1].get('accounts')

df2 = pd.json_normalize(lst_of_dict)

print(df2)
