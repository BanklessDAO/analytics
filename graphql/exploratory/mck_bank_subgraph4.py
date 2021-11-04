from gql import gql, Client
from gql.transport.aiohttp import AIOHTTPTransport

# Select transport with url endpoint
transport = AIOHTTPTransport(
    url="https://api.studio.thegraph.com/query/1121/bankv1/v0.0.5")

# create GraphQL client using defined transport
client = Client(transport=transport, fetch_schema_from_transport=True)

# GraphQL query
query = gql("""
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
            )

# query = gql(
"""
query($first: Int!, $skip: Int!)
{
    transferBanks (first: $first, skip: $skip, orderBy: timestamp, orderDirection: asc, subgraphError: allow) {
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
# )


#page_size = 1000
#skip = 0

'''while True:
    vars = {"first": page_size, "skip": skip}
    # run query on transport
    result = client.execute(query, variable_values=vars)
    skip += page_size

    if not result['transferBanks']:
        break
        print(result) 
'''


# should be same length as 'first' parameter
# print(len(result['transferBanks']))


# run query on transport
result = client.execute(query)
print(result)

# should be same length as 'first' parameter
# print(len(result['transferBanks']))
