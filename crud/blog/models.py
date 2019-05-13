from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    contents = models.TextField()
    author = models.CharField(max_length=50, default="홍길동")

    def __str__(self):
        return self.title
