from django import forms
from .models import Quiz


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('option_one_count', 'option_two_count', 'option_three_count', 'option_four_count')