from django.db import models
from mentorship.mixins import BaseImage, DateTimeMixin
from mentorship.models import Specialization, Teacher


class Course(models.Model, DateTimeMixin):
    name = models.CharField(max_length=150)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    specialization = models.ManyToManyField(Specialization, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"


class Topic(models.Model, DateTimeMixin):
    name = models.CharField(max_length=150)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    image = models.ManyToManyField(BaseImage, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"
