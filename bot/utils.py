import logging

from aiogram.methods import DeleteWebhook

from bot.bot import dp, bot
from bot.content.handlers import rg_msg_hd
from bot.content.middlewares import rg_middlewares
from data.config import BASE_WEBHOOK_URL, WEBHOOK_PATH, WEBHOOK_SECRET
from database import Database


async def start_with() -> None:
    pool_connect = await Database.get_pool_connect()
    if pool_connect is None:
        raise Exception("No pool connected")

    await bot(DeleteWebhook(drop_pending_updates=True))
    await bot.set_webhook(f"{BASE_WEBHOOK_URL}{WEBHOOK_PATH}", secret_token=WEBHOOK_SECRET)

    rg_msg_hd(dp)
    rg_middlewares(dp, pool_connect)
    logging.warning("Bot has been started!")


async def stop_with():
    pool_connect = await Database.get_pool_connect()
    await pool_connect.close()
    logging.warning("Bot has been stopped!")
