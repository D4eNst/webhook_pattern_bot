import logging

import aioredis
import asyncpg
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis

from data.config import db_connection_data, main_db
from data.config import redis_url
from .db import Database

redis = Redis.from_url(redis_url)
# redis = aioredis.from_url(redis_url)
storage = RedisStorage(redis=redis)


# async def get_pool_connect() -> asyncpg.pool.Pool | None:
#     """
#         Returns a pool of database connections with data that is defined in config.py
#         Make sure that you have correctly specified all the data in the .env file.
#         :returns: An instance of ~asyncpg.pool.Pool.
#     """
#
#     pool_connect = None
#
#     logging.info("Creating pull")
#     try:
#         pool_connect = await asyncpg.create_pool(**db_connection_data)
#     except asyncpg.exceptions.InvalidCatalogNameError:
#         logging.info("Creating database")
#         user, password, database, host, port, *_ = db_connection_data.values()
#
#         conn = await asyncpg.connect(user=user, password=password, database=main_db, host=host, port=port)
#         await conn.execute(f'CREATE DATABASE {database}')
#         await conn.close()
#
#         pool_connect = await asyncpg.create_pool(**db_connection_data)
#         async with pool_connect.acquire() as connect:
#             await Database(connect).create_tables()
#     except Exception as e:
#         logging.error(f"Error in creating pool:\n{e}")
#
#     return pool_connect
