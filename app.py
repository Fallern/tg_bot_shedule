import logging
import asyncio

from aiogram import executor

import handlers
from database import connect, models
from loader import dp
from utils.service import convert

from utils.service.update_logic import load_on_start_all_files_xlsx
from utils.service.update_logic import check_shedule
from utils.set_bot_commands import set_default_commands
from utils.notify_admins import on_startup_notify


async def on_startup(dispatcher):
    logging.basicConfig(level=logging.INFO)
    await connect.database_init()
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    await load_on_start_all_files_xlsx()
    await convert.start_load_all_files_png()
    asyncio.create_task(check_shedule())


async def on_shutdown(dispatcher):
    await connect.database_close()
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
