from django.db import models
from django.utils import timezone
# Create your models here.

class Todo(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200,blank=True)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField()

    def __str__(self):
        return f"{self.title}"