# using python-dotenv method
import json
import requests
import os
from dotenv import load_dotenv
load_dotenv()


query = """query
{
     PoapEventV1s(first: 100, where: {name: {contains: "Bankless DAO Community"}}) {
      	data {
      	  id,
          name,
          virtualEvent,
          description,
          endsAt
      	}
      }
}
"""


def run_query(q):
    request = requests.post('https://prod-content-gateway-api.herokuapp.com/api/v1/graphql'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. Return code is {},     {}'.format(
            request.status_code, query))


result = run_query(query)

# print results
print('Print POAP API Query Result - {}'.format(result))
