import logging

from aiogram import Dispatcher

from data.config import ADMIN_ID


async def on_startup_notify(dp: Dispatcher):
    try:
        text = "Bot start"
        await dp.bot.send_message(chat_id=ADMIN_ID, text=text)
    except Exception as err:
        logging.exception(err)
