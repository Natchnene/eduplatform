from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .consts import create_base_image, create_topic
from .serializers import TopicSerializer
from mentorship.consts import create_course, create_teacher


class CreateTopicTest(APITestCase):
    def setUp(self):
        self.teacher = create_teacher()
        self.course = create_course(self.teacher)
        self.base_image = create_base_image()

    def test_create_topic(self):
        url = reverse("topic-list")
        response = self.client.post(url,
                                    data={
                                        "name": "TestTopic",
                                        "description": "TestDescription",
                                        "course": self.course.id,
                                        "image": [self.base_image.id]},
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadTopicTest(APITestCase):
    def setUp(self):
        self.topic = create_topic()

    def test_read_topic_list(self):
        url = reverse("topic-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_topic_detail(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTopicTest(APITestCase):
    def setUp(self):
        self.topic = create_topic()
        self.data = TopicSerializer(self.topic).data
        self.data.update = {"name": "NewTestTopic"}

    def test_update_topic(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.put(url, self.data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTopicTest(APITestCase):
    def setUp(self):
        self.topic = create_topic()

    def test_update_topic(self):
        url = reverse("topic-detail", args=[self.topic.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
