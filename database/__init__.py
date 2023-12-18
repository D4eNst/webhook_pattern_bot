from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis

from bot.bot import config
from .db import Database

redis = Redis.from_url(config.REDIS_URL)
storage = RedisStorage(redis=redis)
