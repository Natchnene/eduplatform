from django.contrib import admin

from .mixins import BaseImage
from .models import Group, Specialization, Student, Teacher, User

admin.site.register(User)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Specialization)
admin.site.register(BaseImage)
