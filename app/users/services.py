from app.service.base import BaseService
from app.users.models import User


class UserService(BaseService[User]):
    model = User
