from django.shortcuts import render, get_object_or_404
from .models import Course


def all_courses(request):
    # to show all courses
    courses = Course.objects.all()
    return render(request, "courses.html", {"courses": courses})


def one_course(request, pk):
    # to open course page
    course = get_object_or_404(Course, pk=pk)

    return render(request, "course.html", {'course': course})
