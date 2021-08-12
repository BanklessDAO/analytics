import requests

from pprint import pprint

# function to use requests.posts to make API call to subgraph url


def run_query(q):
    # end point to make request
    # https://gateway.thegraph.com/api/[api-key]/subgraphs/id/0x0a0319671f2d3c18fb55ab555b48bc01f27747a4-0
    # replace [api-key]
    # deposit GRT in billing
    # then query
    request = requests.post('https://gateway.thegraph.com/api/[api-key]/subgraphs/id/0x0a0319671f2d3c18fb55ab555b48bc01f27747a4-0'
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
# see UMA Mainnet in The Graph "Playground" for query explanations
# source: https://thegraph.com/explorersubgraph?id=0x0a0319671f2d3c18fb55ab555b48bc01f27747a4-0&view=Playground


query = """

{
    users(first: 5) {
    id
    address
    countReveals
    countRetrievals
  }
  priceIdentifiers(first: 5) {
    id
    isSupported
    priceRequests {
      id
    }
  }
}
"""

result = run_query(query)

# print results
print('Print Result - {}'.format(result))
print('################')

# pretty print
pprint(result)
