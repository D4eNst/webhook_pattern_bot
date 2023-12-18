from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio.client import Redis
from data.config import Config

config = Config()

redis = Redis.from_url(config.REDIS_URL)
storage = RedisStorage(redis=redis)

bot = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(storage=storage)
