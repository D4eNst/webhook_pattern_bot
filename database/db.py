# from .models import
import logging

import asyncpg
from data.config import db_connection_data, MAIN_DB


class Database:
    pool_connect = None

    def __init__(self, connect: asyncpg.pool.Pool = None):
        self.connect = connect
        if connect is None:
            self.connect = Database.pool_connect
        self.cursor = self.connect

    @classmethod
    async def get_pool_connect(cls) -> asyncpg.pool.Pool | None:
        """
            Returns a pool of database connections with data that is defined in config.py
            Make sure that you have correctly specified all the data in the .env file.
            :returns: An instance of ~asyncpg.pool.Pool.
        """
        if cls.pool_connect is not None:
            return cls.pool_connect
        pool_connect = None

        logging.info("Creating pull")
        try:
            pool_connect = await asyncpg.create_pool(**db_connection_data)
        except asyncpg.exceptions.InvalidCatalogNameError:
            logging.info("Creating database")
            user, password, database, host, port, *_ = db_connection_data.values()

            conn = await asyncpg.connect(user=user, password=password, database=MAIN_DB, host=host, port=port)
            await conn.execute(f'CREATE DATABASE {database}')
            await conn.close()

            pool_connect = await asyncpg.create_pool(**db_connection_data)
            async with pool_connect.acquire() as connect:
                await Database(connect).create_tables()
        except Exception as e:
            logging.error(f"Error in creating pool:\n{e}")

        cls.pool_connect = pool_connect
        return pool_connect

    async def create_tables(self) -> None:
        await self.connect.execute("""
            CREATE TABLE IF NOT EXISTS table_name(
                id INT PRIMARY KEY,
                first INT,
                second TEXT
            )""")
