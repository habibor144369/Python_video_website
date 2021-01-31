from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.
class Video(models.Model):
    date = models.DateField()
    time = models.TimeField()
    caption = models.CharField(max_length=200)
    video = EmbedVideoField()  # same like models.URLField()
    def __str__(self):
        return self.caption
    

class Detail(models.Model):
    date = models.DateField()
    time = models.TimeField()
    caption = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/%y")
    detail = models.TextField()
    def __str__(self):
        return self.caption


    