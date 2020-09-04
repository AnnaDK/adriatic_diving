from django.test import TestCase
from courses.models import Course

# Create your tests here.


class CoursesCourseTests(TestCase):
    """tests that we'll run against our activities models """

    def test_str(self):
        test_name = Course(name='')
        self. assertEqual(str(test_name), 'An course')