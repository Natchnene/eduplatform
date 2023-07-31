from django.db import models


class DateTimeMixin:
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)


class BaseImage(models.Model):
    image = models.ImageField(null=True, blank=True)
