from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course


# Create your views here.


def all_courses(request):
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})


def one_course(request, pk):
    course = get_object_or_404(Course, pk=pk)

    return render(request, "course.html", {'course': course})
    