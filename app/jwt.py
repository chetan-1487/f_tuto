import jwt
import datetime
from .config import Config

def decode_jwt(token):
    try:
        decoded = jwt.decode(token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGO])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
