from datetime import date

from pydantic import BaseModel


class SBooking(BaseModel):
    id: int
    room_id: int
    customer_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int
