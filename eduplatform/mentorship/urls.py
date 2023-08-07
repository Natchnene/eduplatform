from django.urls import include, path
from rest_framework import routers

from .endpoints import StudentViewSet, TeacherViewSet, UserViewSet

router = routers.SimpleRouter()
router.register("userviewset", UserViewSet)
router.register("teacherviewset", TeacherViewSet)
router.register("studentviewset", StudentViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
