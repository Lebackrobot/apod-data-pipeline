import sqlalchemy

from os import getenv
from dotenv import load_dotenv

load_dotenv(override=True)

DATABASE_URL = getenv('DATABASE_URL')

try:
    db_engine = sqlalchemy.create_engine(DATABASE_URL, echo=True)
    db_connection = db_engine.connect()

except Exception as error:
    print(f"Fail to db_connect: {error}")