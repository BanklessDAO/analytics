import pandas as pd

data = [
    {
        "id": 2220,
        "fancyId": "bankless-dao-community-call-1-2021",
        "name": "Bankless DAO Community Call #1",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 2346,
        "fancyId": "bankless-dao-community-call-2-2021",
        "name": "Bankless DAO Community Call #2",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 2501,
        "fancyId": "bankless-dao-community-call-3-2021",
        "name": "Bankless DAO Community Call #3",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 2655,
        "fancyId": "bankless-dao-community-call-4-2021",
        "name": "Bankless DAO Community Call #4",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 2867,
        "fancyId": "bankless-dao-community-call-5-2021",
        "name": "Bankless DAO Community Call #5",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 3155,
        "fancyId": "bankless-dao-community-call-6-2021",
        "name": "Bankless DAO Community Call #6",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 3400,
        "fancyId": "bankless-dao-community-call-7-2021",
        "name": "Bankless DAO Community Call #7",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 3642,
        "fancyId": "bankless-dao-community-call-s1c1-2021",
        "name": "Bankless DAO Community Call S1C1",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 3925,
        "fancyId": "bankless-dao-community-call-s1c2-2021",
        "name": "Bankless DAO Community Call S1C2",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 4203,
        "fancyId": "bankless-dao-community-call-s1c3-2021",
        "name": "Bankless DAO Community Call S1C3",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 4498,
        "fancyId": "bankless-dao-community-call-s1c4-2021",
        "name": "Bankless DAO Community Call S1C4",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 4824,
        "fancyId": "bankless-dao-community-call-s1c5-2021",
        "name": "Bankless DAO Community Call S1C5",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 5253,
        "fancyId": "bankless-dao-community-call-s1c6-2021",
        "name": "Bankless DAO Community Call S1C6",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 5570,
        "fancyId": "bankless-dao-community-call-s1c7-2021",
        "name": "Bankless DAO Community Call S1C7",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 5572,
        "fancyId": "bankless-dao-community-call-s1c8-2021",
        "name": "Bankless DAO Community Call S1C8",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 6451,
        "fancyId": "bankless-dao-community-call-s1c9-2021",
        "name": "Bankless DAO Community Call S1C9",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 6837,
        "fancyId": "bankless-dao-community-call-s1c10-2021",
        "name": "Bankless DAO Community Call S1C10",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 6838,
        "fancyId": "bankless-dao-community-call-s1c11-2021",
        "name": "Bankless DAO Community Call S1C11",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 6839,
        "fancyId": "bankless-dao-community-call-s1c12-2021",
        "name": "Bankless DAO Community Call S1C12",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 6841,
        "fancyId": "bankless-dao-community-call-s1c13-2021",
        "name": "Bankless DAO Community Call S1C13",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 9141,
        "fancyId": "bankless-dao-community-call-participant-2021",
        "name": "Bankless DAO Community Call Participant",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 9174,
        "fancyId": "bankless-dao-community-call-s1c14-2021",
        "name": "Bankless DAO Community Call S1C14",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 10722,
        "fancyId": "bankless-dao-community-call-16-2021",
        "name": "Bankless DAO Community Call #16",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 11236,
        "fancyId": "bankless-dao-community-call-17-2021",
        "name": "Bankless DAO Community Call #17",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 12043,
        "fancyId": "bankless-dao-community-call-25-2021",
        "name": "Bankless DAO Community Call #25",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 12810,
        "fancyId": "bankless-dao-community-call-19-2021",
        "name": "Bankless DAO Community Call #19",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 12833,
        "fancyId": "bankless-dao-community-call-26-2021",
        "name": "Bankless DAO Community Call #26",
        "year": 2021,
        "createdAt": -1
    },
    {
        "id": 13519,
        "fancyId": "bankless-dao-community-call-27-2021",
        "name": "Bankless DAO Community Call #27",
        "year": 2021,
        "createdAt": -1
    }
]


df = pd.DataFrame(data)

print(df)

# write to csv
# df.to_csv('community_call_events.csv')
