from aiogram import Bot, types, Dispatcher
import redis
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from data import config
from data.config import REDIS_DB, REDIS_HOST, REDIS_PORT, REDIS_PASSWORD

bot = Bot(token=config.API_TOKEN_TELEGRAM, parse_mode=types.ParseMode.HTML)

storage = RedisStorage2(host=REDIS_HOST, port=int(REDIS_PORT), password=REDIS_PASSWORD, db=int(REDIS_DB), state_ttl=360,
                        data_ttl=360)

dp = Dispatcher(bot, storage=storage)

redis_client = redis.Redis(host=REDIS_HOST, port=int(REDIS_PORT), password=REDIS_PASSWORD, db=int(REDIS_DB),
                           decode_responses=True)
