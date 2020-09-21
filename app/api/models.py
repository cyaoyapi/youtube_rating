from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    """Model representing a youtube video"""

    title = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    url = models.URLField(max_length=200)
    category = models.CharField(max_length=50)
    subcategory = models.TextField(max_length=50)
    author = models.TextField(max_length=50)


class Rating(models.Model):
    """Model representing a rate on a youtube video"""

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comments = models.TextField(max_length=300)

    class Meta:
        unique_together = (('video', 'user'),)
        index_together = (('video', 'user'),)
