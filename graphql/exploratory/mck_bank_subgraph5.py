#import psycopg2
import sqlalchemy
from sqlalchemy import create_engine

# connect to Posgres (table: stg_subgraph_bank)
# pip3 install psycopg2
# pip3 install SQLAlchemy

# db_string = 'postgresql://user:password@localhost/mydatabase'
db_string = 'postgresql://user:password@localhost/mydatabase'

db = create_engine(db_string)

# Create test table
db.execute(
    "CREATE TABLE IF NOT EXISTS films (title text, director text, year text)")

db.execute(
    "INSERT INTO films (title, director, year) VALUE ('Dune', 'Squid Game', 'Halloween', 'Foundation')")

# Read
result_set = db.execute("SELECT * FROM films")
for r in result_set:
    print(r)
