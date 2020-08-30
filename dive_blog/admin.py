from django.contrib import admin
from .models import BlogPost, BlogComment, BlogAdvert

admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(BlogAdvert)