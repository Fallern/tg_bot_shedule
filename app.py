import asyncio
import logging

from aiogram import executor

import handlers
from database import connect
from loader import dp
from utils.service.update_logic import load_on_start_all_files_xlsx
from utils.service.update_logic import check_shedule


async def on_startup(dispatcher):
    logging.basicConfig(level=logging.INFO)
    await connect.database_init()
    await load_on_start_all_files_xlsx()
    asyncio.create_task(check_shedule())
    # await convert.start_load_all_files_png()


async def on_shutdown(dispatcher):
    await connect.database_close()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
