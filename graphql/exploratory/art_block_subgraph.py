import requests
import json

from pprint import pprint

# function to use requests.posts to make API call to subgraph url


def run_query(q):
    # end point to make request
    # https://gateway.thegraph.com/api/[api-key]/subgraphs/id/0x3c3cab03c83e48e2e773ef5fc86f52ad2b15a5b0-0
    # replace [api-key]
    # deposit GRT in billing
    # then query
    request = requests.post('https://gateway.thegraph.com/api/[api-key]/subgraphs/id/0x3c3cab03c83e48e2e773ef5fc86f52ad2b15a5b0-0'
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
  projects(first: 100) {
    id
    artistName
    artistAddress
    name
    license
    locked
    royaltyPercentage
    website
  }
}
"""

result = run_query(query)

# print results
print('Print Art Blocks Result - {}'.format(result))
print('################')

# pretty print
pprint(result)

# save 'result' to json file
print("Save result as JSON file:")
print("#######JSON########")
with open('./art_blocks.json', 'w', encoding='utf8') as f:
    json.dump(result, f, ensure_ascii=False)
