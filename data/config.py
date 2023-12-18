import logging
import os

# Needed adding .env file with 5 constants:
# POSTGRES_USER
# POSTGRES_PASSWORD
# REDIS_PASSWORD
# TOKEN
# ADMIN_ID

TOKEN = os.environ["TOKEN"]
ADMIN_ID = int(os.environ["ADMIN_ID"])
BASE_WEBHOOK_URL = "https://test1.d4enst.tech"
WEBHOOK_SECRET = "WEBHOOK_SECRET"
WEBHOOK_PATH = "/webhook"

REDIS_HOST = "redis"
REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]
REDIS_PORT = 6379
REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"

POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_USER = os.environ["POSTGRES_USER"]
DATABASE = "Change_your_database_name"
MAIN_DB = "postgres"
POSTGRES_HOST = "postgres_db"

db_connection_data = {
    "user": POSTGRES_USER,
    "password": POSTGRES_PASSWORD,
    "database": DATABASE,
    "host": POSTGRES_HOST,
    "port": 5432,
    "command_timeout": 60
}


class Config:
    _initialize = False
    if not _initialize:
        try:
            TOKEN = os.environ["TOKEN"]
            ADMIN_ID = int(os.environ["ADMIN_ID"])
            REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]
            POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
            POSTGRES_USER = os.environ["POSTGRES_USER"]
            _initialize = True
        except Exception as e:
            logging.error(f"Error reading environment variables. Make sure that all variables are present "
                          f"and they are correct. The initial error:\n{e}")

    def __init__(self,
                 redis_host="redis",
                 redis_port=6379,
                 postgres_host="postgres_db",
                 postgres_port=5432,
                 database="Change_your_database_name",
                 ):
        """
        change docker-compose.yml if you change something other than database
        :param redis_host:
        :param redis_port:
        :param postgres_host:
        :param postgres_port:
        :param database:
        """
        self.REDIS_HOST = redis_host

        self.REDIS_PORT = redis_port
        self.REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"

        self.POSTGRES_HOST = postgres_host
        self.POSTGRES_PORT = postgres_port
        self.DATABASE = database
        self.MAIN_DB = "postgres"

