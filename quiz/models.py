from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=10, default='')
    question = models.TextField()
    option_one = models.CharField(max_length=200)
    option_two = models.CharField(max_length=200)
    option_three = models.CharField(max_length=200)
    option_four = models.CharField(max_length=200)
    option_one_count = models.BooleanField(default=True)
    option_two_count = models.BooleanField(default=True)
    option_three_count = models.BooleanField(default=True)
    option_four_count = models.BooleanField(default=True)
    answer = models.CharField(max_length=200, default='')
    
    def __str__(self):
        return self.name