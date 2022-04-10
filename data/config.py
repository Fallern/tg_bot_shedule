import os
from dotenv import load_dotenv

load_dotenv()

DB_NAME = os.environ['DB_NAME']
DB_PORT = os.environ['PORT']
DB_HOST = os.environ['HOST']
DB_USER = os.environ['USER']
DB_PASSWORD = os.environ['PASSWORD']

REDIS_PORT = os.environ['REDIS_PORT']
REDIS_HOST = os.environ['REDIS_HOST']
REDIS_DB = os.environ['REDIS_DB']
REDIS_PASSWORD = None  # os.environ['REDIS_PASSWORD']

API_TOKEN_TELEGRAM = os.environ['API_TOKEN']
CLOUDCONVERT_TOKEN = os.environ['CLOUDCONVERT_TOKEN']
TOKEN = os.environ['TOKEN']
ADMIN_ID = os.environ['ADMIN_ID']

DB_CONFIG = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "database": DB_NAME,
                "host": DB_HOST,
                "password": DB_PASSWORD,
                "port": DB_PORT,
                "user": DB_USER,
            }
        }
    },
    "apps": {
        "models": {
            "models": ["database.models"],
            "default_connection": "default",
        }
    },
}
