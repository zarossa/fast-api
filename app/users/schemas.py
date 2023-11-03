from pydantic import BaseModel, EmailStr


class SUser(BaseModel):
    id: int
    email: EmailStr
    hashed_password: str


class SUserAuth(BaseModel):
    email: EmailStr
    password: str
