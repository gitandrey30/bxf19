
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings_db import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME



DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
# print(DATABASE_URL)
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(engine)
session = Session()



