import jwt
import datetime
from .config import Config

def create_jwt(data, expires_in=60):
    payload = {
        "data": data,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=expires_in)
    }
    token = jwt.encode(payload, Config.JWT_SECRET, algorithm=Config.JWT_ALGO)
    return token

def decode_jwt(token):
    try:
        decoded = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGO])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
