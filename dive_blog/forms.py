from django import forms
from .models import BlogPost, BlogComment


class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment
        fields = ('name', 'text',)