from django.shortcuts import render
from django.views import generic

def index(request):
    return render(request, 'workout/workout.html')