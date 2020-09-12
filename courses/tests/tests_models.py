from django.test import TestCase
from courses.models import Course

# if Course model is passing values correctly 


class TestModels(TestCase):

    def test_course_model(self):
        course = Course.objects.create(
            name='course',
            description='course description',
            minimum_age='10',
            certification_prior='certification',
            academic_sessions='academic_sessions',
            confined_water='confined_water',
            openwater_dives='openwater_dives',
            maximum_depth='40',
            duration='duration',
            price=360,
            image='image.png'
        )
        course.save()

        self.assertEquals(course.name, 'course')
        self.assertEquals(course.description, 'course description')
        self.assertEquals(course.minimum_age, '10')
        self.assertEquals(course.certification_prior, 'certification')
        self.assertEquals(course.academic_sessions, 'academic_sessions')
        self.assertEquals(course.confined_water, 'confined_water')
        self.assertEquals(course.openwater_dives, 'openwater_dives')
        self.assertEquals(course.maximum_depth, '40')
        self.assertEquals(course.duration, 'duration')
        self.assertEquals(course.price, 360)
        self.assertEquals(course.image, 'image.png')