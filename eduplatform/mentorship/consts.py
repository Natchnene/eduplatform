from .annotations import UserAnnotation
from .models import Group, Specialization, Student, Teacher, User

USER_DATA = {"password": "qwerty", "first_name": "TestName", "last_name": "TestSurname", "email": "test@email.com"}


def create_user() -> UserAnnotation:
    user = User.objects.create_user(password="qwerty", first_name="TestName", last_name="TestSurname", email="test@email.com")
    return user


SPECIALIZATION_DATA = {"specialization": "TestSpecialization"}


def create_specialization():
    specialization = Specialization.objects.create(specialization="TestSpecialization")
    return specialization


def create_teacher():
    user = create_user()
    specialization = create_specialization()
    teacher = Teacher.objects.create(user=user.id, specialization=[specialization])
    return teacher
