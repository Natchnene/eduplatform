from .models import Course, Topic
from mentorship.consts import create_course, create_teacher
from mentorship.mixins import BaseImage
from unittest.mock import Mock

import mock
from django.core.files import File


def create_base_image():
    file_mock = mock.MagicMock(spec=File)
    image = BaseImage(image=file_mock)
    # mock = Mock()
    # mock.return_value = "TestImage"
    # image.image(mock)
    return image


def create_topic():
    teacher = create_teacher()
    course = create_course(teacher)
    image = create_base_image()
    topic = Topic.objects.create(name="TestTopic", description="TestDescription", course=course)
    topic.image.add(image.id)
    return topic

