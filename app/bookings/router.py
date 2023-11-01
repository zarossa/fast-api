from fastapi import APIRouter

from app.bookings.schemas import SBooking
from app.bookings.services import BookingService

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingService.find_all()
