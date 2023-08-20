from django.urls import include, path
from rest_framework import routers

from .endpoints import (
    AnswerTypeViewSet,
    AnswerViewSet,
    ArticleViewSet,
    CourseViewSet,
    QuestionViewSet,
    TestViewSet,
    TopicViewSet,
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
]
