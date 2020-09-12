from django.test import TestCase
from django import forms
from accounts.forms import ( UserLoginForm, UserRegistrationForm )




class Test_User_Login_Registration_Forms(TestCase):
#we are testing if the form is valid
    def test_user_login_form(self):
        form = UserLoginForm(data={
            'username':'max@mail.com',
            'password': '12345678',
        })
        self.assertTrue(form.is_valid())

    def test_user_registration_form(self):
        form = UserRegistrationForm(data={
            'username':'max',
            'email': 'max@mail.com',
            'password1': '12345678',
            'password2': '12345678',
        })
        self.assertTrue(form.is_valid())

    def test_user_login_form_invalid_password(self):
        form = UserLoginForm(data={
            'username':'max@mail.com',
            'password': '',
        })
        self.assertFalse(form.is_valid())
    
    def test_user_login_form_invalid_username(self):
        form = UserLoginForm(data={
            'username': '',
            'password': '12345678',
        })
        self.assertFalse(form.is_valid())

    def test_user_registration_form_invalid(self):
        form = UserRegistrationForm(data={
            'username': 'Max',
            'email': 'max@mail.com',
            'password1': '12345678',
            'password2': '1234567',
        })
        self.assertFalse(form.is_valid())

    def test_no_username_user_registration_form(self):
     
        form = UserRegistrationForm(data={
            'username': ' ',
            'email': 'max@mail.com',
            'password1': 'password',
            'password2': 'password',
        })
        self.assertFalse(form.is_valid())
