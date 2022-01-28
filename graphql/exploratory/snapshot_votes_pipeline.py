import requests
import json
import pandas as pd
from pprint import pprint

query = """
{
        votes(first: 10000, where: {proposal: "0xabccf8394b35e92043a4055f8430f1babd44fdc763849ad0158441073578a62e"}) {
          id
          voter
          created
          choice
          __typename
          proposal {
            id
          }
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
print('Print Snapshot Votes Result - {}'.format(result))
print('################')

# pretty print
# pprint(result)

# convert to list, then df
result_list = list(result.items())
lst_of_dict = result_list[0][1].get('votes')
latest_df = pd.json_normalize(lst_of_dict)

pprint(latest_df)

# reset index
# increment index



##-------------- ONE TIME EVENT ------------ ##

# Manually run GraphQL query,
# concatenate all dfs
# reset_index() TWICE
# change column names
# write to csv

# concatenate 17 dataframes into one

# Proposal ids
# df        QmdoixPMMT76vSt6ewkE87JZJywS1piYsGC3nJJpcrPXKS  -- 1353 rows
# df1        QmbCCAH3WbAFJS4FAUTvpWGmtgbaeMh1zoKgocdt3ZJmdr   -- 597 rows
# df2        QmYvsZ7AU2XyhpBL8g4QRQbLRX6uU3t5CHNdFQbs5r7ypJ   -- 588 rows
# df3        QmQX2DQcDTZzCpM6DTVNJutQJwWXtxJDTMpBoFjbnaM9i2   -- 558 rows
# df4        QmXrfAHMoRcu5Vy3DsRTfokqLBTEKR6tqKVecLvkgw5NZf   -- 509 rows
# df5        QmTCfpZirT9mUrJD8rMZKpguiCpDKASFCnGQFpk6eyUk77   -- 136 rows
# df6        QmWoNKRmdn2hr1vKaoLkmuKWRQ611AiuB22JPpnDPae2m6   -- 196 rows
# df7        QmZLGKBRQTUcdET7aPsnFNJJoY2Z885j3c1813trEsUGck   -- 109 rows
# df8        QmSTXHWP7bjaxT9aAuoFNkaCn5Ptx7GajEDDekoBccd5Uf   -- 752 rows
# df9        Qmdthz7Anz7g2aJJAewNqm3gQnssP5NkS2StNKELvArQkk   -- 650 rows
# df10       QmYmHuawgkCZxVMo6EHq5s2WxQrSwTYZeBGRfFkc1xeW5f   -- 535 rows
# df11       QmWwN1CeDPLcvCVkDuBiYmaaNcRhfrUzFYhBixF2B3ntJU   -- 523 rows
# df12       QmcL7qZ4nA3NoTukMVXXZeramGA8QiqQSpdBFAuRRht5T6   -- 395 rows
# df13       QmeUcnL5FTpF2ah2CCph6DZGqJzG19coT9b3ECLAvBxPH2   -- 480 rows
# df14       QmVm6jzr7yDRiBmmkvCQ1MFw4jTaiJcME6ZNBp4QuU1DHA   -- 464 rows
# df15       QmZhncmagTnWXjvX17Kmm1f25D33CPAw6f1UQBo7fzm6UQ   -- 341 rows
# df16       QmWjyeUFLmvVLg3fYeNWLjPscy6u4JU2tv8A1E1qjfDi2L   -- 435 rows
# df17    0xabccf8394b35e92043a4055f8430f1babd44fdc763849ad0158441073578a62e    -- 506 rows
# concat_frame 9127 rows


# frames = [df, df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14, df15, df16, df17]
# concat_frames = pd.concat(frames)

# reset_index TWICE to get 0 - 9126 rows
# concat_frames_1 = concat_frames.reset_index()
# concat_frames_2 = concat_frames_1.reset_index()

# concat_frames_3 = concat_frames_2[[
#    'level_0', 'id', 'voter', 'created', 'choice', '__typename', 'proposal.id']]

# change column names level_0 = id, id = vote_id, proposal.id = proposal_id
# concat_frames_4 = concat_frames_3.rename(
#    columns={'level_0': 'id', 'id': 'vote_id', 'proposal.id': 'proposal_id'}, inplace=False)

# print(concat_frames_4)

# write to csv
# concat_frames_4.to_csv('bankless_snapshot_votes.csv')

##-------------- ONE TIME EVENT ------------ ##