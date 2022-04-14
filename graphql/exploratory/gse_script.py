import json
import pandas as pd

# Graphql Query https://hub.snapshot.org/
"""
    {
        votes(first: 10000, where: {proposal: "0xb93ef13c7f48841d50191124a6e76c3bdd099edc501b6325a495ee70db77fe5a"}) {
          id
          voter
          created
          choice
          __typename
    			proposal {
            id
            space {
              id
            }
          }
    }

"""

# note: query saved as json file in data directory
# this script opens the file and converts to dataframe, then csv
with open("../data/gse_vote.json") as json_file:
    json_data = json.load(json_file)

df = pd.json_normalize(json_data)
print(df)

# uncomment to write csv
# df.to_csv('gse_vote.csv')
