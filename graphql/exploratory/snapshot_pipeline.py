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

query2 = """
{
        votes(first: 10000, where: {proposal: "QmdoixPMMT76vSt6ewkE87JZJywS1piYsGC3nJJpcrPXKS"}) {
          id
          voter
          created
          choice
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

# print(df)
# df.columns
# df.loc

# select subset of columns
# reset_index() twice to get index in ascending order
sub_df = df[['id', 'title', 'start', 'end']]
# sort in ascending order by 'start' timestamp
sub_df2 = sub_df.sort_values('start').reset_index()
sub_df3 = sub_df2.reset_index()
sub_df4 = sub_df3[['level_0', 'id', 'title', 'start', 'end']]  # remove index
sub_df5 = sub_df4.rename(columns={'level_0': 'index'}, inplace=False)
print(sub_df5)


# capture list of proposal id
# lst_proposal_id = list(df['id'])
# sub_df5.to_csv('bankless_snapshot_proposals.csv')
