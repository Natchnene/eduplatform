from rest_framework.serializers import ModelSerializer

from .models import Answer, AnswerType, Article, Course, Question, Test, Topic


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"


class AnswerTypeSerializer(ModelSerializer):
    class Meta:
        model = AnswerType
        fields = "__all__"


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"
