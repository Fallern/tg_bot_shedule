from tortoise import Tortoise, run_async
import logging
from data import config


async def database_init():
    url = f"postgres://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"
    await Tortoise.init(
        config=config.DB_CONFIG
    )
    await Tortoise.generate_schemas()
    logging.info("DataBase inited!")


async def database_close():
    await Tortoise.close_connections()
    logging.info("DataBase closed!")
