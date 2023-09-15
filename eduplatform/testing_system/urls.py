from django.urls import include, path, re_path
from rest_framework import routers

from .endpoints import (
    AnswerTypeViewSet,
    AnswerViewSet,
    ArticleViewSet,
    CoursesStudentAPIView,
    CourseViewSet,
    QuestionViewSet,
    RecommendationAPIView,
    TestViewSet,
    TopicViewSet,
    CoursesSpecializationAPIView,
    QuestionsTestAPIView,
    ArticlesCourseAPIView,
    TestsTeacherAPIView,
)

router = routers.SimpleRouter()
router.register("courseviewset", CourseViewSet)
router.register("topicviewset", TopicViewSet)
router.register("articleviewset", ArticleViewSet)
router.register("testviewset", TestViewSet)
router.register("answertypeviewset", AnswerTypeViewSet)
router.register("questionviewset", QuestionViewSet)
router.register("answerviewset", AnswerViewSet)


urlpatterns = [
    path("", include(router.urls)),
    re_path("student/(?P<id>[^/.]+)/course", CoursesStudentAPIView.as_view(), name="courses_student"),
    re_path("student/(?P<id>[^/.]+)/recommendation", RecommendationAPIView.as_view(), name="recommendation_courses"),
    re_path("specialization/(?P<id>[^/.]+)/courses", CoursesSpecializationAPIView.as_view(), name="courses_specialization"),
    re_path("test/(?P<id>[^/.]+)/questions", QuestionsTestAPIView.as_view(), name="questions_test"),
    re_path("course/(?P<id>[^/.]+)/articles", ArticlesCourseAPIView.as_view(), name="articles_course"),
    re_path("teacher/(?P<id>[^/.]+)/test", TestsTeacherAPIView.as_view(), name="tests_teacher"),
]
