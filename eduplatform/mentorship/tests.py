from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .consts import SPECIALIZATION_DATA, USER_DATA, create_specialization, create_user, create_teacher
from .serializers import SpecializationSerializer, UserSerializer, TeacherSerializer


class CreateUserTest(APITestCase):
    def test_create_user(self):
        url = reverse("user-list")
        response = self.client.post(url, data=USER_DATA, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_read_user_list(self):
        url = reverse("user-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_user_detail(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.data = UserSerializer(self.user).data
        self.data.update({"first_name": "newTestName"})

    def test_update_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_delete_user(self):
        url = reverse("user-detail", args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateSpecializationTest(APITestCase):
    def test_create_specialization(self):
        url = reverse("specialization-list")
        response = self.client.post(url, data=SPECIALIZATION_DATA, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadSpecializationTest(APITestCase):
    def setUp(self):
        self.specialization = create_specialization()

    def test_read_specialization_list(self):
        url = reverse("specialization-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_specialization_detail(self):
        url = reverse("specialization-detail", args=[self.specialization.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateSpecializationTest(APITestCase):
    def setUp(self):
        self.specialization = create_specialization()
        self.data = SpecializationSerializer(self.specialization).data
        self.data.update = {"specialization": "NewTestSpecialization"}

    def test_update_specialization(self):
        url = reverse("specialization-detail", args=[self.specialization.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteSpecializationTest(APITestCase):
    def setUp(self):
        self.specialization = create_specialization()

    def test_delete_specialization(self):
        url = reverse("specialization-detail", args=[self.specialization.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateTeacherTest(APITestCase):
    def setUp(self):
        self.user = create_user()
        self.specialization = create_specialization()

    def test_create_teacher(self):
        url = reverse("teacher-list")
        response = self.client.post(url,
                                    data={
                                        "user": self.user.id,
                                        "specialization": [self.specialization.id]})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTeacherTest(APITestCase):
    def setUp(self):
        self.teacher = create_teacher()

    def test_read_teacher_list(self):
        url = reverse("teacher-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_teacher_detail(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTeacherTest(APITestCase):
    def setUp(self):
        self.teacher = create_teacher()
        self.data = TeacherSerializer(self.teacher).data
        self.specialization = create_specialization()
        self.data.update = {"specialization": [self.specialization.id]}

    def test_update_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTeacherTest(APITestCase):
    def setUp(self):
        self.teacher = create_teacher()

    def test_delete_teacher(self):
        url = reverse("teacher-detail", args=[self.teacher.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
