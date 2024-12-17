from src.configs.logging_config import logging
from dotenv import load_dotenv
from os import getenv
import sqlalchemy

log = logging.getLogger(__name__)

load_dotenv(override=True)

DATABASE_URL = getenv('DATABASE_URL')

try:
    db_engine = sqlalchemy.create_engine(DATABASE_URL)
    db_connection = db_engine.connect()

except Exception as error:
    log.error(f"Fail to db_connect: {error}")