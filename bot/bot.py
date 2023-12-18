from aiogram import Dispatcher, Bot
from database import storage
from data.config import Config

config = Config()
bot = Bot(token=config.TOKEN, parse_mode='HTML')
dp = Dispatcher(storage=storage)
