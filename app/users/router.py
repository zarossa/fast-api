from fastapi import APIRouter, HTTPException

from app.users.auth import get_password_hash
from app.users.schemas import SUserRegister
from app.users.services import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Users"]
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UserService.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    hashed_password = get_password_hash(user_data.password)
    await UserService.add(email=user_data.email, hashed_password=hashed_password)
