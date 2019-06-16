from django.contrib import admin

from .models import Question, Result


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    pass
