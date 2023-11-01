from fastapi import APIRouter
from sqlalchemy import select

from app.bookings.models import Booking
from app.database import async_session_maker

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings():
    async with async_session_maker() as session:
        query = select(Booking.__table__.columns)
        result = await session.execute(query)
        return result.mappings().all()

