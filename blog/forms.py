from django import forms
from .models import Comment


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text', 'created_date')