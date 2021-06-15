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
query = """

{
  events(where: { id: 2655 }) {
    id
    tokens {
      id
      owner {
        id
      }
      transfers {
        id
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
