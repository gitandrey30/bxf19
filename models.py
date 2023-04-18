from sqlalchemy import MetaData, Table, VARCHAR, Integer, Column, TIMESTAMP

from config_db import engine

metadata = MetaData()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', VARCHAR(100)),
    Column('data', TIMESTAMP),
)

metadata.create_all(engine)

# def __repr__(self):
#     return f'<user> {self.name}, {self.date}'