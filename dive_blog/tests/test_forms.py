from django.test import TestCase
from dive_blog.forms import BlogCommentForm


class TestForms(TestCase):

    def test_blog_comment_form(self):
        # test if the form is valid
        form = BlogCommentForm(data={
            'name': 'Max',
            'text': ' a comment.'
        })
        self.assertTrue(form.is_valid())
  # test if the form is missing one field
    
    def test_message_for_missing_name(self):
        form = BlogCommentForm(data={
            'name': ' ',
            'text': 'a comment.'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])
 # test if the form is missing one field
    
    def test_blog_comment_form_no_text(self):
        
        form = BlogCommentForm(data={
            'name': 'Max ',
            'text': ' '
        })
        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['text'], [u'This field is required.'])
