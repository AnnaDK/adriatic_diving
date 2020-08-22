from django.db import models

from django.db import models
from django.utils import timezone


class Post(models.Model):
     
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=500, default='')
    post_content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='images', blank=True, null=True)
  

    def __unicode__(self):
        return self.title
          