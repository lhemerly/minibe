from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from models.user import User, UserInDB, UserNew
from controllers.security_utils import (
    get_password_hash,
    create_access_token,
    decode_token,
    verify_password,
    Token,
)

from controllers.users import (
    get_user,
    get_user_by_email,
    get_user_by_full_name,
    create_user,
    delete_user,
)

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/signup")
async def new_user(user: UserNew) -> User:
    if await get_user(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists"
        )

    if await get_user_by_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists"
        )

    if await get_user_by_full_name(user.full_name):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Full name already exists"
        )

    hashed_password = await get_password_hash(user.password)

    return await create_user(
        UserInDB(
            **user.dict(),
            hashed_password=hashed_password,
        )
    )


@router.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    user = await get_user(form_data.username)
    verified_password = await verify_password(form_data.password, user.hashed_password)

    if not user or not verified_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password",
        )

    if not user.verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User not verified"
        )

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="User disabled"
        )

    access_token = await create_access_token(
        data={"sub": user.username}, expires_delta=None
    )

    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)) -> User:
    user = await decode_token(token)
    user = user.get("sub")
    user = await get_user(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bad token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


@router.get("/users/me/signoff")
async def signoff(token: str = Depends(oauth2_scheme)) -> dict:
    user = await decode_token(token)
    user = user.get("sub")
    user = await get_user(user)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bad token",
            headers={"WWW-Authenticate": "Bearer"},
        )

    await delete_user(user.username)

    return {"message": "User deleted"}
