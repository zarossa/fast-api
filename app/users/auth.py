from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.users.services import UserService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hash_password: str) -> bool:
    return pwd_context.verify(plain_password, hash_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_KEY, settings.JWT_ALGO
    )
    return encoded_jwt


async def auth_user(email: EmailStr, password: str):
    user = await UserService.find_one_or_none(email=email)
    if user and verify_password(password, user.hashed_password):
        return user
