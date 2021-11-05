# coding: utf-8
from sqlalchemy.orm import Session
from sqlalchemy import text
import sqlalchemy
from sqlalchemy import create_engine

# establish connection
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)
print(engine)

# hello world
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

# commit to the database 'as you go'
with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )
    conn.commit()

# 'begin once'
# begin once (as opposed to 'commit as you go') as usually preferred as its more succinct and indicates the intention of the block up front
# note: BEGIN (implicit) means SQLAlchemy did not actually send any command to the database
# this is still DDL - data definition language (not yet DML, data manipulation language)
with engine.begin() as conn:
    conn.execute(
        text("INSERT INTO some_table (x,y) VALUES (:x, :y)"),
        [{"x": 6, "y": 8}, {"x": 9, "y": 10}]
    )


# FETCHING ROWS
with engine.connect() as conn:
    result = conn.execute(text("SELECT x, y FROM some_table"))
    for row in result:
        print(f"x: {row.x} y: {row.y}")

print(result)

# Tuple Assignment
result = conn.execute(text("SELECT x, y FROM some_table"))
# Row objects act like Python named tuples
# Variety of ways to access Rows: Tuple Assignment, Integer Index, Attribute Name, Mapping Access

# SENDING PARAMETERS
with engine.connect() as conn:
    result = conn.execute(
        text("SELECT x, y FROM some_table WHERE y > :y"),
        {"y": 2}
    )
    for row in result:
        print(f"x: {row.x} y: {row.y}")

# Sending Multiple Parameters
with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUE (:x, :y)"),
        [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
    )
    conn.commit()

with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
    )
    conn.commit()

# DBAPI = Database API specification
# Bundling Parameters with a Statement
stmt = text(
    "SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)

with engine.connect() as conn:
    result = conn.execute(stmt)
    for row in result:
        print(f"x: {row.x} y: {row.y}")

stmt = text(
    "SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y").bindparams(y=6)

with Session(engine) as session:
    result = session.execute(stmt)
    for row in result:
        print(f"x: {row.x} y: {row.y}")

with Session(engine) as session:
    result = session.execute(
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x": 9, "y": 11}, {"x": 13, "y": 15}]
    )
    session.commit()

# NEXT Working with Database Metadata
