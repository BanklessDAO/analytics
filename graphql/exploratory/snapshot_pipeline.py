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
print('Print Snapshot Proposal Result - {}'.format(result))
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

# write dataframe to CSV (one-time event)
# sub_df5.to_csv('bankless_snapshot_proposals.csv')


# capture list of proposal id
# lst_proposal_id = list(df['id'])

# Proposal ids
# 0        QmdoixPMMT76vSt6ewkE87JZJywS1piYsGC3nJJpcrPXKS
# 1        QmbCCAH3WbAFJS4FAUTvpWGmtgbaeMh1zoKgocdt3ZJmdr
# 2        QmYvsZ7AU2XyhpBL8g4QRQbLRX6uU3t5CHNdFQbs5r7ypJ
# 3        QmQX2DQcDTZzCpM6DTVNJutQJwWXtxJDTMpBoFjbnaM9i2
# 4        QmXrfAHMoRcu5Vy3DsRTfokqLBTEKR6tqKVecLvkgw5NZf
# 5        QmTCfpZirT9mUrJD8rMZKpguiCpDKASFCnGQFpk6eyUk77
# 6        QmWoNKRmdn2hr1vKaoLkmuKWRQ611AiuB22JPpnDPae2m6
# 7        QmZLGKBRQTUcdET7aPsnFNJJoY2Z885j3c1813trEsUGck
# 8        QmSTXHWP7bjaxT9aAuoFNkaCn5Ptx7GajEDDekoBccd5Uf
# 9        Qmdthz7Anz7g2aJJAewNqm3gQnssP5NkS2StNKELvArQkk
# 10       QmYmHuawgkCZxVMo6EHq5s2WxQrSwTYZeBGRfFkc1xeW5f
# 11       QmWwN1CeDPLcvCVkDuBiYmaaNcRhfrUzFYhBixF2B3ntJU
# 12       QmcL7qZ4nA3NoTukMVXXZeramGA8QiqQSpdBFAuRRht5T6
# 13       QmeUcnL5FTpF2ah2CCph6DZGqJzG19coT9b3ECLAvBxPH2
# 14       QmVm6jzr7yDRiBmmkvCQ1MFw4jTaiJcME6ZNBp4QuU1DHA
# 15       QmZhncmagTnWXjvX17Kmm1f25D33CPAw6f1UQBo7fzm6UQ
# 16       QmWjyeUFLmvVLg3fYeNWLjPscy6u4JU2tv8A1E1qjfDi2L
# 17    0xabccf8394b35e92043a4055f8430f1babd44fdc763849ad0158441073578a62e
