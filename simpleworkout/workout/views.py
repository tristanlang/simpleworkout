from django.shortcuts import render
from django.views import generic
from random import randint
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

# signup view
# login view
#
# workout view
# history view
# add new view
# preferences view
# xxxxx about view xxxxx

def about(request):
    return render(request, 'workout/about.html')

def workout(request):
    # 0. if no user, display the workout for the tristan user
    # 0.5. if time of request is after workout has been completed show the alternate
    # 0.75. if time of request is after midnight, show the new workout and add to workout db (steps 1-5)
    # 1. get user (from cookies) -- http://stackoverflow.com/questions/1622793/django-cookies-how-can-i-set-them
    # 2. get user log to see what past 7 workouts were
    # 3. see if preferences are met
    # 4. otherwise, randomly choose from the categories based on preferences
    # 5. no strength work two consecutive days

    # temporarily just use tristanlang as all users
    user = User.objects.get_by_natural_key('tristanlang')
    requestdatetime = timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())

    # check for log with today's date and current user
    log = Log.objects.filter({'date__gte': requestdatetime.date(), 'user': user})
    if not log:
        # display today's workout if it exists
        # if it does not exist (past midnight), create it
    else:
        # display the completed workout with notes
        # state that the new workout will be posted at midnight
        #    -already in the template


    return render(request, 'workout.html')