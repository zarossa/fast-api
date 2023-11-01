from typing import TypeVar, Generic

from sqlalchemy import select

from app.database import async_session_maker


T = TypeVar("T")


class BaseService(Generic[T]):
    model: T = None

    @classmethod
    async def find_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            results = await session.execute(query)
            return results.mappings().all()
