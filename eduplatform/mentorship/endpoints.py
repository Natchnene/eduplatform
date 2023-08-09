from rest_framework import permissions, viewsets

from .mixins import BaseImage
from .models import Group, Specialization, Student, Teacher, User
from .serializers import (
    BaseImageSerializer,
    GroupSerializer,
    SpecializationSerializer,
    StudentSerializer,
    TeacherSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]


class TeacherViewSet(viewsets.ModelViewSet):
    serializer_class = TeacherSerializer
    queryset = Teacher.objects.all()
    permission_classes = [permissions.AllowAny]


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [permissions.AllowAny]


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = [permissions.AllowAny]


class SpecializationViewSet(viewsets.ModelViewSet):
    serializer_class = SpecializationSerializer
    queryset = Specialization.objects.all()
    permission_classes = [permissions.AllowAny]


class BaseImageViewSet(viewsets.ModelViewSet):
    serializer_class = BaseImageSerializer
    queryset = BaseImage.objects.all()
    permission_classes = [permissions.AllowAny]
