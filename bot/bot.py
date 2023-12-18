from aiogram import Dispatcher, Bot
from database import storage
from data.config import TOKEN


bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher(storage=storage)
