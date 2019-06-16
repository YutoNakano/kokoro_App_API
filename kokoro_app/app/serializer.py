from rest_framework import serializers

from .models import Question, Result

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id','title', 'description', 'comment', 'status', 'image_url')


class ResultSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Result
        fields = ('id','title', 'description', 'comment', 'status', 'image_url', 'url')
