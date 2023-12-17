import logging

from bot.bot import dp
from bot.content.handlers import rg_msg_hd
from bot.content.middlewares import rg_middlewares
from database import get_pool_connect


async def start_with() -> None:
    pool_connect = await get_pool_connect()
    rg_msg_hd(dp)
    rg_middlewares(dp, pool_connect)
    logging.warning("Bot has been started!")


async def stop_with():
    logging.warning("Bot has been stopped!")
