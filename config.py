import os
from dotenv import load_dotenv


load_dotenv()


DB_NAME = os.environ['DB_NAME']
PORT = os.environ['PORT']
HOST = os.environ['HOST']
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']