from .models import Course, Topic
from mentorship.consts import create_course, create_teacher
from mentorship.mixins import BaseImage
from unittest.mock import Mock


def create_base_image():
    image = BaseImage()
    mock = Mock()
    image.image(mock)
    return image


def create_topic():
    teacher = create_teacher()
    course = create_course(teacher)
    image = create_base_image()
    topic = Topic.objects.create(name="TestTopic", description="TestDescription", course=course)
    topic.image.add(image.id)
    return topic

