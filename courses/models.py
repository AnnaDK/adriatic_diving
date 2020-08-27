from django.db import models


class Course(models.Model):

    name = models.CharField(max_length=260, default='')
    description = models.TextField()
    minimum_age = models.CharField(max_length=100, default='')
    certification_prior = models.CharField(max_length=100, default='')
    academic_sessions = models.CharField(max_length=100, default='')
    confined_water = models.CharField(max_length=100, default='')
    openwater_dives = models.CharField(max_length=100, default='')
    maximum_depth = models.CharField(max_length=100, default='')
    duration = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    online_offer_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
