from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


class BlogPost(models.Model):
     
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, unique=False, default='')
    short_description = models.TextField(max_length=500)
    post_content = RichTextField()
    created_date = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, default='')
    image = models.ImageField(upload_to='images', blank=True,
                              default='images/None/no-img.jpg')
    small_image = models.ImageField(upload_to='images', blank=True,
                                    default='images/None/no-img.jpg')
    
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
  
    def __unicode__(self):
        return self.title
          

class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_date']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text


class BlogAdvert(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', blank=True,
                              default='images/None/no-img.jpg')
    link = models.URLField(max_length=250, default='')

    def __unicode__(self):
        return self.title

