from itertools import chain

from rest_framework import permissions, viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .mixins import BaseImage
from .models import Group, Specialization, Student, Teacher, User
from .serializers import (
    BaseImageSerializer,
    GroupSerializer,
    GroupStudentSerializer,
    SpecializationSerializer,
    StudentSerializer,
    TeacherSerializer,
    TeachersStudentsSerializer,
    UserSerializer,
    LoginSerializer
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


class StudentsGroupAPIView(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        group_id = self.kwargs["id"]
        student = Student.objects.filter(group__in=group_id)
        return student


class TeachersSpecializationAPIView(ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        specialization_id = self.kwargs["id"]
        teacher = Teacher.objects.filter(specialization=specialization_id)
        return teacher


class TeacherGroupAPIView(ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        group_id = self.kwargs["id"]
        return Teacher.objects.filter(group__in=group_id)


class RecommendationTeacherAPIView(ListAPIView):
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        student_id = self.kwargs["id"]
        group = Group.objects.filter(student=student_id)
        student_teacher = Teacher.objects.filter(id__in=group.values("teacher_id"))
        all_teachers = Teacher.objects.filter(specialization__in=student_teacher.values("specialization"))
        recommendation_teacher = all_teachers.exclude(id__in=student_teacher.values("id"))
        return recommendation_teacher


class TeachersStudentsCourseAPIView(ListAPIView):
    serializer_class = TeachersStudentsSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        course_id = self.kwargs["id"]
        teachers = Teacher.objects.filter(course__in=course_id)
        group = Group.objects.filter(course=course_id)
        students = Student.objects.filter(id__in=group.values("student"))
        queryset = chain(teachers, students)
        if isinstance(queryset, chain):
            return queryset


class LoginAPIView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        user = request.data.get("user", {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
