from django import forms
from .models import Quiz


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ('option_one_checkbox', 'option_two_checkbox',
                  'option_three_checkbox', 'option_four_checkbox')
