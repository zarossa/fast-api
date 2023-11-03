from fastapi import APIRouter, Depends

from app.bookings.schemas import SBooking
from app.bookings.services import BookingService
from app.users.dependencies import get_current_user
from app.users.schemas import SUser

router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"]
)


@router.get("")
async def get_bookings(user: SUser = Depends(get_current_user)) -> list[SBooking]:
    return await BookingService.find_all(user_id=user.id)
