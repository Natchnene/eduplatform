from rest_framework.serializers import ModelSerializer

from .mixins import BaseImage
from .models import Group, Specialization, Student, Teacher, User


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


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class SpecializationSerializer(ModelSerializer):
    class Meta:
        model = Specialization
        fields = "__all__"


class BaseImageSerializer(ModelSerializer):
    class Meta:
        model = BaseImage
        fields = "__all__"
