from rest_framework.serializers import ModelSerializer

from .models import Student, Teacher, User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
