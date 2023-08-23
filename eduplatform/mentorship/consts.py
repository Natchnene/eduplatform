from .models import User
from .annotations import UserAnnotation

USER_DATA = {
    "password": "qwerty",
    "first_name": "TestName",
    "last_name": "TestSurname",
    "email": "test@email.com"}


def create_user() -> UserAnnotation:
    user = User.objects.create_user(
        password="qwerty",
        first_name="TestName",
        last_name="TestSurname",
        email="test@email.com")
    return user
