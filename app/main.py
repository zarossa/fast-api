# from dataclasses import dataclass
from datetime import date
from typing import Optional

import uvicorn
from fastapi import FastAPI, Query, Depends
from pydantic import BaseModel, field_validator
from pydantic.dataclasses import dataclass
from pydantic_core.core_schema import FieldValidationInfo

from app.bookings.router import router as router_bookings

app = FastAPI()

app.include_router(router_bookings)


class SHotel(BaseModel):
    address: str
    name: str
    stars: int


@dataclass
class HotelSearchArgs:
    location: str
    date_from: date
    date_to: date
    stars: Optional[int] = Query(None, ge=1, le=5)
    has_spa: Optional[bool] = None

    @field_validator('date_to')
    def check_dates(cls, date_to: date, info: FieldValidationInfo) -> date:
        if 'date_from' in info.data and date_to < info.data['date_from']:
            raise ValueError('Date from less than date to')
        return date_to


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

    @field_validator('date_to')
    def check_dates(cls, date_to: date, info: FieldValidationInfo) -> date:
        if 'date_from' in info.data and date_to < info.data['date_from']:
            raise ValueError('Date from less than date to')
        return date_to


@app.get('/hotels')
def get_hotels(
    search_args: HotelSearchArgs = Depends()
) -> list[SHotel]:
    hotel2 = SHotel(address='qw', name='12', stars=1)
    hotels = [hotel2,
              hotel2]
    print(search_args.stars)
    return hotels


@app.post('/booking')
def add_booking(booking: SBooking):
    pass


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
