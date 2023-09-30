from .models import Course, Topic
from mentorship.consts import create_course, create_teacher
from mentorship.mixins import BaseImage


def create_base_image():
    image = BaseImage.objects.create("image_2023-07-30_21-55-43.png")
    return image


def create_topic():
    teacher = create_teacher()
    course = create_course(teacher)
    image = create_base_image()
    topic = Topic.objects.create(name="TestTopic", description="TestDescription", course=course)
    topic.image.add(image.id)
    return topic

