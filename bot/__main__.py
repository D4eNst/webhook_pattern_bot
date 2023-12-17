import logging

from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from .bot import dp, bot
from .utils import start_with, stop_with

logging.basicConfig(level=logging.INFO)


def start_bot():
    # register handlers and start/stop functions
    dp.startup.register(start_with)
    dp.shutdown.register(stop_with)

    # # getting main pool connect
    # pool_connect = await get_pool_connect()
    # if pool_connect is None:
    #     return
    #
    # rg_msg_hd(dp)
    # rg_middlewares(dp, pool_connect)

    try:
        # await bot.get_updates(offset=-1)
        # await bot(DeleteWebhook(drop_pending_updates=True))
        # await dp.start_polling(bot)
        app = web.Application()

        webhook_requests_handler = SimpleRequestHandler(
            dispatcher=dp,
            bot=bot,
            secret_token="WEBHOOK_SECRET",
        )

        webhook_requests_handler.register(app, path='/webhook')

        setup_application(app, dp, bot=bot)

        web.run_app(app, host='0.0.0.0', port=8080)
        logging.info("Webhook started")
    finally:
        # await pool_connect.close()
        # await bot.session.close()
        ...


if __name__ == "__main__":
    try:
        start_bot()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
