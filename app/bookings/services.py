from app.bookings.models import Booking
from app.service.base import BaseService


class BookingService(BaseService[Booking]):
    model = Booking
