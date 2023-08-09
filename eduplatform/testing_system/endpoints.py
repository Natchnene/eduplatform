from rest_framework import permissions, viewsets

from .models import Answer, AnswerType, Article, Course, Question, Test, Topic
from .serializers import (
    AnswerSerializer,
    AnswerTypeSerializer,
    ArticleSerializer,
    CourseSerializer,
    QuestionSerializer,
    TestSerializer,
    TopicSerializer,
)


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny]


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = [permissions.AllowAny]


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [permissions.AllowAny]


class TestViewSet(viewsets.ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = [permissions.AllowAny]


class AnswerTypeViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerTypeSerializer
    queryset = AnswerType.objects.all()
    permission_classes = [permissions.AllowAny]


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Course.objects.all()
    permission_classes = [permissions.AllowAny]


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [permissions.AllowAny]
