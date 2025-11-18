import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  Database_URL = os.getenv("DATABASE_URL")
  Secret_key = os.getenv("DATABASE_URL")
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATION")