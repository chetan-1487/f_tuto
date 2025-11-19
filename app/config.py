import os
from dotenv import load_dotenv

load_dotenv()

class Config:
  SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
  SECRET_KEY = os.getenv("DATABASE_URL")
  SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATION")
  JWT_SECRET = os.getenv("JWT_SECRET")
  JWT_ALGO = os.getenv("JWT_ALGO")