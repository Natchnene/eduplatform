from django.db import models
from mentorship.mixins import DateTimeMixin
from mentorship.models import Specialization, Teacher


class Course(models.Model, DateTimeMixin):
    name = models.CharField(max_length=150)
    description = models.TextField()
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    specialization = models.ManyToManyField(Specialization, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"
