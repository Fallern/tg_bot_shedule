from aiogram import Bot, types, Dispatcher
import redis

from data import config

bot = Bot(token=config.API_TOKEN_TELEGRAM, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

redis_client = redis.Redis(decode_responses=True)
