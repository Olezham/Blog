from django.db import models
from django.utils import timezone


# Create your models ere.
class News(models.Model):
    title = models.CharField(max_length=50)
    intro = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

