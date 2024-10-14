from django.db import models
from django.utils import timezone

# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=200)  # Field for the video title
    url = models.URLField()  # Field for the video URL
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
