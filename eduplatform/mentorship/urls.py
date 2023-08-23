from django.urls import include, path, re_path
from rest_framework import routers

from .endpoints import (
    BaseImageViewSet,
    GroupStudentAPIView,
    GroupViewSet,
    RecommendationTeacherAPIView,
    SpecializationViewSet,
    StudentsGroupAPIView,
    StudentViewSet,
    TeacherGroupAPIView,
    TeachersSpecializationAPIView,
    TeachersStudentsCourseAPIView,
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
    path("group_student/", GroupStudentAPIView.as_view(), name="groups_students"),
    re_path("group/(?P<id>[^/.]+)/student", StudentsGroupAPIView.as_view(), name="students_group"),
    re_path("specialization/(?P<id>[^/.]+)/teacher", TeachersSpecializationAPIView.as_view(), name="teachers_specialization"),
    re_path("group/(?P<id>[^/.]+)/teacher", TeacherGroupAPIView.as_view(), name="teacher_group"),
    re_path("student/(?P<id>[^/.]+)/teacher/recommendation", RecommendationTeacherAPIView.as_view(), name="recommendation_teacher"),
    re_path("course/(?P<id>[^/.]+)/teachers_students", TeachersStudentsCourseAPIView.as_view(), name="teachers_students_teacher"),
]
