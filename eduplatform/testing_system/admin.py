from django.contrib import admin

from .models import Answer, AnswerType, Article, Course, Question, Test, Topic

admin.site.register(Course)
admin.site.register(Topic)
admin.site.register(Article)
admin.site.register(Test)
admin.site.register(AnswerType)
admin.site.register(Answer)
admin.site.register(Question)
