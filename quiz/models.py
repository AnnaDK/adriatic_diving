from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=10, default='')
    question = models.TextField()
    option_one = models.CharField(max_length=200)
    option_two = models.CharField(max_length=200)
    option_three = models.CharField(max_length=200)
    option_four = models.CharField(max_length=200)
    option_one_checkbox = models.BooleanField(default=False)
    option_two_checkbox = models.BooleanField(default=False)
    option_three_checkbox = models.BooleanField(default=False)
    option_four_checkbox = models.BooleanField(default=False)
    answer = models.CharField(max_length=200, default='')

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name
