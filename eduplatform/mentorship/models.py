from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager
from .mixins import DateTimeMixin


class User(AbstractBaseUser, PermissionsMixin, DateTimeMixin):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_("Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Specialization(models.Model, DateTimeMixin):
    specialization = models.CharField(_("specialization"), max_length=200, blank=True)

    def __str__(self):
        return f"{self.specialization}"


class Teacher(models.Model, DateTimeMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialization = models.ManyToManyField(Specialization)

    def __str__(self):
        return f"{self.pk} - {self.user.email}"


class Student(models.Model, DateTimeMixin):
    rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.user.email}"


class Group(models.Model, DateTimeMixin):
    name = models.CharField(_("name group"), max_length=150)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    student = models.ManyToManyField(Student, blank=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"
