from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth import authenticate

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


class GroupStudentSerializer(ModelSerializer):
    class Meta:
        model = Group

    def to_representation(self, object):
        match object.__class__.__name__:
            case "Student":
                serializer = StudentSerializer(object)
            case "Group":
                serializer = GroupSerializer(object)
            case _:
                raise Exception("Nothing to serialize. Check input data.")
        return serializer.data


class TeachersStudentsSerializer(ModelSerializer):
    class Meta:
        model = Teacher

    def to_representation(self, object):
        match object.__class__.__name__:
            case "Teacher":
                serializer = TeacherSerializer(object)
            case "Student":
                serializer = StudentSerializer(object)
            case _:
                raise Exception("Nothing to serialize. Check input data.")
        return serializer.data


class LoginSerializer(Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(username=email, password=password)

        if not all(email or password or user):
            raise serializers.ValidationError("DATA IS NOT CORRECT")
        try:
            if not user.is_active:
                raise serializers.ValidationError("USER IS NOT ACTIVE")
        except AttributeError:
            raise serializers.ValidationError("DATA IS NOT CORRECT2")

        return {"email": user.email, "token": user.token}




