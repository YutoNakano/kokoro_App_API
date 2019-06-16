import django_filters
from rest_framework import viewsets, filters

from .models import Question, Result
from .serializer import QuestionSerializer, ResultSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

