from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis

from data.config import REDIS_URL
from .db import Database

redis = Redis.from_url(REDIS_URL)
storage = RedisStorage(redis=redis)
