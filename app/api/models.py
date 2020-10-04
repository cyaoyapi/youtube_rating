from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Video(models.Model):
    """Model representing a youtube video"""

    title = models.CharField(max_length=80)
    description = models.TextField(max_length=300)
    url = models.URLField()
    category = models.CharField(max_length=50)
    subcategory = models.TextField(max_length=50)
    author = models.TextField(max_length=50)

    def ratings_average(self):
        sum = 0
        ratings = Rating.objects.filter(video=self)
        if len(ratings) > 0:
            for rating in ratings:
                sum = + rating.stars 
            return sum / len(ratings)
        else:
            return 0
    
    def comments_list(self):
        """ Return the list of comments """ 

        return [rating.comments for rating in Rating.objects.filter(video=self)]
        

class Rating(models.Model):
    """Model representing a rate on a youtube video"""

    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comments = models.TextField(max_length=300)

    class Meta:
        unique_together = (('video', 'user'),)
        index_together = (('video', 'user'),)
