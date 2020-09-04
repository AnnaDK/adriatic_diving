from django.test import TestCase
from .models import BlogPost, BlogComment, BlogAdvert


class TestModels(TestCase):

    def test_blogpost_model(self):
        blogpost = BlogPost.objects.create(
            title='first_post',
            short_description='first_post_description',
            post_content='first_post_content',
            author='company',
            created_date='2020-05-30',
            views='0',
            tag='post',
            image='image.png',
            small_image='small_image.png'
        )
        blogpost.save()
        self.assertEquals(blogpost.title, 'first_post')
        self.assertEquals(blogpost.short_description, 'first_post_description')
        self.assertEquals(blogpost.author, 'company')
        self.assertEquals(blogpost.post_content, 'first_post_content')
        self.assertEquals(blogpost.created_date, '2020-05-30')
        self.assertEquals(blogpost.views, '0')
        self.assertEquals(blogpost.tag, 'post')
        self.assertEquals(blogpost.image, 'image.png')
        self.assertEquals(blogpost.small_image, 'small_image.png')
