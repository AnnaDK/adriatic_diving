from django.test import TestCase
from .models import Activity

# Create your tests here.


class ActivityTests(TestCase):
    """tests that we'll run against our activities models """

    def test_str(self):
        test_name = Activity(name='An activity')
        self. assertEqual(str(test_name), 'An activity')