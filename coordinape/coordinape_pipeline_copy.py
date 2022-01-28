import requests
from pprint import pprint
import os
import pandas as pd

# database connection
import time
from sqlalchemy import create_engine
import psycopg2

# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

# authorization & header
auth_token = os.environ.get('AUTH_TOKEN')
HEADER = {'Authorization': f'{auth_token}'}

# ----- Data Endpoints

# Coordinape Round -- OG Bankless(June): Circle id 24
response24 = requests.get(
    'https://api.coordinape.com/api/v2/token-gifts?circle_id=24', headers=HEADER)

# return list of 7135 dictionaries
result24 = response24.json()
# use pandas to convert list of dict to dataframe
df24 = pd.json_normalize(result24)


# Coordinape Round -- Bankless L1: Circle id 305
response305 = requests.get(
    'https://api.coordinape.com/api/v2/token-gifts?circle_id=305', headers=HEADER)

# return & convert list of dict to dataframe using pandas
result305 = response305.json()
df305 = pd.json_normalize(result305)


# Coordinape Round -- Bankless L2: Circle id 492
response492 = requests.get(
    'https://api.coordinape.com/api/v2/token-gifts?circle_id=492', headers=HEADER)
result492 = response492.json()
df492 = pd.json_normalize(result492)


# Coordinape Round -- Bankless GP: Circle id 878
response878 = requests.get(
    'https://api.coordinape.com/api/v2/token-gifts?circle_id=878', headers=HEADER)
result878 = response878.json()
df878 = pd.json_normalize(result878)

# concatenate dataframes
frames = [df24, df305, df492, df878]
concat_frames = pd.concat(frames)

# reset index twice
concat_frames_2 = concat_frames.reset_index()
concat_frames_3 = concat_frames_2.reset_index()

# select specific columns
concat_frames_4 = concat_frames_3[['level_0', 'id', 'recipient_address', 'sender_address',
                                   'recipient_id', 'sender_id', 'tokens', 'circle_id', 'epoch_id',
                                   'dts_created']]

# change column name 'dts_created' -> 'timestamp'
concat_frames_5 = concat_frames_4.rename(
    columns={'level_0': 'id', 'id': 'coord_id', 'dts_created': 'timestamp'}, inplace=False)
print(concat_frames_5)
print(f"concat_frames_5 is a {type(concat_frames_5)}")

# INPUT DATABASE CONNECTION STRING
conn_string = os.environ.get('CONN_STRING')
print(conn_string)

# perform to_sql test and print results
db = create_engine(conn_string)
conn = db.connect()


# Perform COPY test and print results
sql = '''
COPY coordinape_rounds_3
FROM 'coordinape_pipe_v3.csv'
DELIMITER ',' CSV;
'''

table_create_sql = '''
CREATE TABLE IF NOT EXISTS coordinape_rounds_3 (id                  BIGINT,
                                                coord_id            BIGINT,
                                                recipient_address   VARCHAR(200),
                                                sender_address      VARCHAR(200),
                                                recipient_id        BIGINT,
                                                sender_id           BIGINT,
                                                tokens              BIGINT,
                                                circle_id           BIGINT,
                                                epoch_id            BIGINT,
                                                timestamp           TIMESTAMP,
                                                PRIMARY KEY (coord_id))
'''

pg_conn = psycopg2.connect(conn_string)
cur = pg_conn.cursor()
cur.execute(table_create_sql)
cur.execute('TRUNCATE TABLE coordinape_rounds_3')

start_time = time.time()
# create .csv file
concat_frames_5.to_csv('coordinape_pipe_v3.csv')
cur.execute(sql)
pg_conn.commit()
cur.close()
print("COPY duration: {} seconds".format(time.time() - start_time))


# close connection
conn.close()


# ERROR
# InsufficientPrivilege: must be superuser or a member of the pg_read_server_files role to COPY from a file
# HINT:  Anyone can COPY to stdout or from stdin. psql's \copy command also works for anyone.
