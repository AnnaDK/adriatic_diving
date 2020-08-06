from django.shortcuts import render
from .models import Activity

# Create your views here.
def all_activities(request):
    activities = Activity.objects.all()
    return render(request, "activities.html", {"activities": activities})


def one_activity(request):
    activity = Activity.objects.all()
    return render(request, "activity.html", {"activity": activity})