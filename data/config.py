import logging
import os


class Config:
    _initialize = False
    if not _initialize:
        try:
            TOKEN = os.environ["TOKEN"]
            ADMIN_ID = int(os.environ["ADMIN_ID"])
            REDIS_PASSWORD = os.environ["REDIS_PASSWORD"]
            POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
            POSTGRES_USER = os.environ["POSTGRES_USER"]
            BASE_WEBHOOK_URL = os.environ["BASE_WEBHOOK_URL"]
            WEBHOOK_SECRET = os.environ["WEBHOOK_SECRET"]
            WEBHOOK_PATH = os.environ["WEBHOOK_PATH"]
            _initialize = True
        except Exception as e:
            logging.error(f"Error reading environment variables. Make sure that all variables are present "
                          f"and they are correct. The initial error:\n{e}")

    def __init__(self,
                 redis_host="redis",
                 redis_port=6379,
                 postgres_host="postgres_db",
                 postgres_port=5432,
                 main_db="postgres",
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
        self.REDIS_URL = f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"

        self.POSTGRES_HOST = postgres_host
        self.POSTGRES_PORT = postgres_port
        self.DATABASE = database.lower()
        self.MAIN_DB = main_db

    def get_db_conn(self, to_main=False):
        return {
            "user": self.POSTGRES_USER,
            "password": self.POSTGRES_PASSWORD,
            "database": self.MAIN_DB if to_main else self.DATABASE,
            "host": self.POSTGRES_HOST,
            "port": self.POSTGRES_PORT,
            "command_timeout": 60
        }
