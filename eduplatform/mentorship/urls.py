from django.urls import include, path
from rest_framework import routers

from .endpoints import (
    BaseImageViewSet,
    GroupViewSet,
    SpecializationViewSet,
    StudentViewSet,
    TeacherViewSet,
    UserViewSet,
)

router = routers.SimpleRouter()
router.register("userviewset", UserViewSet)
router.register("teacherviewset", TeacherViewSet)
router.register("studentviewset", StudentViewSet)
router.register("groupviewset", GroupViewSet)
router.register("specializationviewset", SpecializationViewSet)
router.register("baseimageviewset", BaseImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
