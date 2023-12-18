import logging

from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

from .bot import dp, bot, config
from .utils import start_with, stop_with

logging.basicConfig(level=logging.INFO)


def start_bot():
    # register handlers and start/stop functions
    dp.startup.register(start_with)
    dp.shutdown.register(stop_with)

    try:
        app = web.Application()

        webhook_requests_handler = SimpleRequestHandler(
            dispatcher=dp,
            bot=bot,
            secret_token=config.WEBHOOK_SECRET,
        )

        webhook_requests_handler.register(app, path=config.WEBHOOK_PATH)

        setup_application(app, dp, bot=bot)
        logging.info("Webhook started")
        web.run_app(app, host='0.0.0.0', port=8080)

    except Exception as e:
        logging.error(e)


if __name__ == "__main__":
    try:
        start_bot()
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
