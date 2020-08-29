from django.db import models
from django.utils import timezone


class Post(models.Model):
     
    title = models.CharField(max_length=200)
    short_description = models.TextField(max_length=500, default='')
    post_content = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, default='')
    image = models.ImageField(upload_to='images', blank=True,
                              default='images/None/no-img.jpg')
    small_image = models.ImageField(upload_to='images', blank=True,
                              default='images/None/no-img.jpg')
  
    def __unicode__(self):
        return self.title
          

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
 
    class Meta:
        ordering = ['created_date']

    def __unicode__(self):
        return self.author


class Advert(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True,
                              default='images/None/no-img.jpg')
    link = models.URLField(max_length=250, default='')

    def __unicode__(self):
        return self.title

