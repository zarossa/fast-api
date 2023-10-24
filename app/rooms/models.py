from sqlalchemy import Column, Integer, ForeignKey, String, JSON

from app.database import Base


class Room(Base):
    __tablename__ = "room"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey("hotel.id"))
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)
    image_id = Column(Integer, nullable=False)
