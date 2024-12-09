from fastapi.security import OAuth2PasswordBearer

from pydantic import BaseModel

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    username: str
    email: str = None
    full_name: str = None


class UserNew(User):
    password: str


class UserInDB(User):
    hashed_password: str
    verified: bool = True
    disabled: bool = False
