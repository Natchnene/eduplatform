from itertools import chain

from django.db.models import QuerySet
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView

from .mixins import BaseImage
from .models import Group, Specialization, Student, Teacher, User
from .serializers import (
    BaseImageSerializer,
    GroupSerializer,
    GroupStudentSerializer,
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


class GroupStudentAPIView(ListAPIView):
    serializer_class = GroupStudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        group_queryset = Group.objects.all()
        student_queryset = Student.objects.all()
        queryset = chain(group_queryset, student_queryset)
        if isinstance(queryset, chain):
            return queryset
