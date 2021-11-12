import requests
import json
import pandas as pd
from pprint import pprint


query = """
{
    proposals(first: 1000, skip: 0, where: {space: "banklessvault.eth", state: "all"}) {
        id
        title
        body
        start
        end
        state
        author
        created
        space {
            id
            name
            members
            avatar
            __typename
        }
        __typename
    }
}
"""


def run_query(q):
    request = requests.post('https://hub.snapshot.org/graphql'
                            '',
                            json={'query': query})
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception('Query failed. return code is {}.     {}'.format(
            request.status_code, query))


result = run_query(query)

# print results
print('Print Bank Subgraph Result - {}'.format(result))
print('################')

# pretty print
pprint(result)

# convert to list
result_items = result.items()
result_list = list(result_items)
lst_of_dict = result_list[0][1].get('proposals')
df = pd.json_normalize(lst_of_dict)

print(df)
# df.columns
# df.loc
