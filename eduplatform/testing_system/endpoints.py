from django.db.models import Subquery
from mentorship.models import Group
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView

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


class CoursesStudentAPIView(ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        student_id = self.kwargs["id"]
        group = Group.objects.filter(student=student_id)
        course = Course.objects.filter(id__in=group.values("course_id"))
        return course


class RecommendationAPIView(ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        student_id = self.kwargs["id"]
        group = Group.objects.filter(student=student_id)
        student_courses = Course.objects.filter(id__in=Subquery(group.values("course_id")))
        all_courses = Course.objects.filter(specialization__in=Subquery(student_courses.values("specialization")))
        recommendation = all_courses.exclude(id__in=Subquery(student_courses.values("id")))
        return recommendation


class CoursesSpecializationAPIView(ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        specialization_id = self.kwargs["id"]
        return Course.objects.filter(specialization=specialization_id)


class QuestionsTestAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        test_id = self.kwargs["id"]
        return Question.objects.filter(test=test_id)


class ArticlesCourseAPIView(ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        course_id = self.kwargs["id"]
        return Article.objects.filter(course=course_id)


class TestsTeacherAPIView(ListAPIView):
    serializer_class = TestSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        teacher_id = self.kwargs["id"]
        return Test.objects.filter(teacher=teacher_id)
