from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    comment = models.CharField(max_length=128)
    status = models.BooleanField(default=False)
    image_url = models.ImageField()


class Result(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    comment = models.CharField(max_length=128)
    status = models.BooleanField(default=False)
    image_url = models.ImageField()
    url = models.URLField()