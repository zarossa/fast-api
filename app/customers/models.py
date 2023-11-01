from sqlalchemy.orm import mapped_column, Mapped

from app.database import Base


class Customer(Base):
    __tablename__ = "customer"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]
