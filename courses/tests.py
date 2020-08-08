from django.test import TestCase
from .models import Course

# Create your tests here.


class CourseTests(TestCase):
    """tests that we'll run against our activities models """

    def test_str(self):
        test_name = Course(name='A course')
        self. assertEqual(str(test_name), 'A course')