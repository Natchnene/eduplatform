from .annotations import UserAnnotation
from .models import Group, Specialization, Student, Teacher, User
from testing_system.models import Course

USER_DATA = {"password": "qwerty", "first_name": "TestName", "last_name": "TestSurname", "email": "test@email.com"}


def create_user() -> UserAnnotation:
    user = User.objects.create_user(password="qwerty", first_name="TestName", last_name="TestSurname", email="test@email.com")
    return user


def create_user_2() -> UserAnnotation:
    user = User.objects.create_user(password="qwerty", first_name="TestName", last_name="TestSurname", email="new_test@email.com")
    return user


SPECIALIZATION_DATA = {"specialization": "TestSpecialization"}


def create_specialization():
    specialization = Specialization.objects.create(specialization="TestSpecialization")
    return specialization


def create_teacher():
    user = create_user()
    specialization = create_specialization()
    teacher = Teacher.objects.create(user=user)
    teacher.specialization.add(specialization.id)
    return teacher


def create_student():
    user = create_user_2()
    student = Student.objects.create(rating=0, user=user)
    return student


def create_course(teacher):
    specialization = create_specialization()
    course = Course.objects.create(name="TestCourse", description="TestDescription", teacher=teacher)
    course.specialization.add(specialization.id)
    return course


def create_group():
    teacher = create_teacher()
    student = create_student()
    course = create_course(teacher)
    group = Group.objects.create(name="TestGroup", teacher=teacher, course=course)
    group.student.add(student.id)
    return group
