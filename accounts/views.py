from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages


def index(request):
    """" Return index.html"""
    return render(request, 'index.html')


def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You've been logged out.")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    return render(request, 'login.html')