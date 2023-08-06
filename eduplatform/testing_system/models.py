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


class Article(models.Model, DateTimeMixin):
    name = models.CharField(max_length=150)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"


class Test(models.Model, DateTimeMixin):
    name = models.CharField(max_length=150)
    description = models.TextField()
    is_open = models.BooleanField(default=False)
    time_limit = models.PositiveSmallIntegerField("Time limit in minutes", default=20)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)


class AnswerType(models.Model, DateTimeMixin):
    class Types(models.TextChoices):
        RADIOBUTTON = "radiobutton"
        CHECKBOX = "checkbox"
        INPUT = "input"

    type = models.CharField(default="radiobutton", max_length=15, choices=Types.choices)


class Question(models.Model, DateTimeMixin):
    name = models.CharField(max_length=150)
    test = models.ForeignKey(Test, on_delete=models.SET_NULL, null=True)


class Answer(models.Model, DateTimeMixin):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)
    answer_type = models.ForeignKey(AnswerType, on_delete=models.SET_NULL, null=True)
