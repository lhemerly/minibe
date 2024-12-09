import os
import datetime
from datetime import timedelta, timezone
from passlib.context import CryptContext
import jwt
from pydantic import BaseModel

# read .env file
with open(".env") as f:
    for line in f:
        key, value = line.strip().split("=")
        os.environ[key] = value

SALT = os.environ["SALT"]
ALGORITHM = "HS256"
TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None


async def get_password_hash(password):
    return pwd_context.hash(password)


async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


async def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.datetime.now(timezone.utc) + datetime.timedelta(
            minutes=TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SALT, algorithm=ALGORITHM)
    return encoded_jwt


async def decode_token(token):
    return jwt.decode(token, SALT, algorithms=[ALGORITHM])
