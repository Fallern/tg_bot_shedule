from aiogram import Bot, types, Dispatcher

from data import config

bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)
