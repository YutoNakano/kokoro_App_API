from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    comment = models.CharField(max_length=128, blank=True)
    status = models.BooleanField(default=False)
    image_url = models.CharField(max_length=200, blank=True)


class Result(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    comment = models.CharField(max_length=128, blank=True)
    status = models.BooleanField(default=False)
    image_url = models.CharField(max_length=200, blank=True)
    url = models.URLField(blank=True)