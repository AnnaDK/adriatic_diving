from django.db import models


class Activity(models.Model):
    """ To add activity to the database """
    name = models.CharField(max_length=260, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='activities_images', blank=True)

    def __str__(self):
        return self.name

