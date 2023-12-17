import logging

from bot.bot import dp, bot
from bot.content.handlers import rg_msg_hd
from bot.content.middlewares import rg_middlewares
from database import Database


async def start_with() -> None:
    pool_connect = Database().connect
    if pool_connect is None:
        Database.pool_connect = await Database().get_pool_connect()
        pool_connect = Database.pool_connect
    if pool_connect is None:
        raise Exception("No pool connected")
    rg_msg_hd(dp)
    rg_middlewares(dp, pool_connect)
    logging.warning("Bot has been started!")


async def stop_with():
    await bot.session.close()
    await Database().connect.close()
    logging.warning("Bot has been stopped!")
