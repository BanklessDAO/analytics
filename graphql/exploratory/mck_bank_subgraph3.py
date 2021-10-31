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


# use Pagination with where: $timestamp_gte

# 1st 1000 rows timestamp "1620159318" to "1620178698" May 4 - May 5 df
# 2nd 1000 rows timestamp "1620178698" to "1620195492" May 5 - May 5 df1
# 3rd 1000 rows timestamp "1620195492" to "1620222076" May 5 - May 5 df2
# 4th 1000 rows timestamp "1620222076" to "1620302644" May 5 - May 6 df3
# 5th 1000 rows timestamp "1620302644" to "1620512822" May 6 - May 8 df4
# 6th 1000 rows timestamp "1620512822" to "1621320508" May 8 - May 18 df5
# 7th 1000 rows timestamp "1621320508" to "1622402667" May 18 - May 30 df6
# 8th 1000 rows timestamp "1622402667" to "1622711952" May 30 - June 3 df7
# 9th 1000 rows timestamp "1622711952" to "1623096960" June 3 - June 7 df8
# 10th 1000 rows timestamp "1623096960" to "1623806254" June 7 - June 16 df9
# 11th 1000 rows timestamp "1623806254" to "1624947713" June 16 - June 29 df10
# 12th 1000 rows timestamp "1624947713" to "1626391104" June 29 - July 15 df11
# 13th 1000 rows timestamp "1626391104" to "1627822469" July 15 - Aug 1 df12
# 14th 1000 rows timestamp "1627822469" to "1629015828" Aug 1 - Aug 15 df13
# 15th 1000 rows timestamp "1629015828" to "1630196109" Aug 15 - Aug 29 df14
# 16th 1000 rows timestamp "1630196109" to "1631303170" Aug 29 - Sep 10 df15
# 17th 1000 rows timestamp "1631303170" to "1632091350" Sep 10 - Sep 19 df16
# 18th 1000 rows timestamp "1632091350" to "1632961979" Sep 19 - Sep 30 df17
# 19th 1000 rows timestamp "1632961979" to "1633989634" Sep 30 - Oct 11 df18
# 20th 1000 rows timestamp "1633989634" to "1635403557" Oct 11 - Oct 28 df19
#       552 rows timestamp "1635403557" to "1635654941" Oct 28 - Oct 31 df20

# Last Update: Sun, 31 Oct 2021 04:35:41 GMT
# [20552 rows x 7 columns]

query = """
{
    transferBanks(first: 1000, where: {timestamp_gte: "1635403557"}, orderBy: timestamp, orderDirection: asc, subgraphError: allow) {
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
df20 = pd.json_normalize(lst_of_dict)

print(df20)

# manually concatenate dataframes

# manually update df, df1, df2 and so on...etc.
# frames = [df, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17, df18, df19, df20]
# concat_frames = pd.concat(frames)
# write to csv: concat_frames.to_csv('mck_bank_subgraph.csv')
