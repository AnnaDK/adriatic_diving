from django.test import TestCase
from .models import Post

# Create your tests here.


class PostTests(TestCase):
    """tests that we'll run against our activities models """

    def test_str(self):
        test_name = Post(name='A post')
        self. assertEqual(str(test_name), 'A post')