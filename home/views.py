from django.shortcuts import render

def index(request):
    """ That view will display the index page"""
    return render(request, "index.html")
