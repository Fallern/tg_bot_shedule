from aiogram import Bot, types, Dispatcher
import redis
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data import config

bot = Bot(token=config.API_TOKEN_TELEGRAM, parse_mode=types.ParseMode.HTML)

storage = RedisStorage2(state_ttl=20, data_ttl=20)

dp = Dispatcher(bot, storage=storage)

redis_client = redis.Redis(decode_responses=True)
