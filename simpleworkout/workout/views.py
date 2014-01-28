from django.shortcuts import render
from django.views import generic
import random
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

from workout.models import Log, Workout, Category, Ownership, Preference

# signup view
# login view

todays_workout = None

def weight_first_category(category1, category2):
    if random.randint(0,2):
        return random.choice(Workout.objects.filter('category' == category1))
    else:
        return random.choice(Workout.objects.filter('category' == category2))

def choose_workout(user, requestdatetime):
    today = requestdatetime.date()
    try:
        history = Log.objects.all().order_by('-date')[:7]
    except:
        history = Log.objects.all().order_by('-date')
    lastworkout = history[0]

    cardio = Category.objects.get(category='Cardio')
    strength = Category.objects.get(category='Strength')
    circuit = Category.objects.get(category='Circuit')

    if lastworkout.workout.category == cardio:
        if len(history) > 3 and history[2].workout.category == strength:
            workout = weight_first_category(circuit, strength)
        elif len(history) > 3 and history[2].workout.category == circuit:
            workout = weight_first_category(strength, circuit)
        else:
            workout = random.choice(random.choice(Workout.objects.filter(category=strength)),
                random.choice(Workout.objects.filter(category=circuit)))
    else:
        workout = random.choice(Workout.objects.filter(category=cardio))
    return (today, workout)



def about(request):
    return render(request, 'workout/about.html')



def workout(request):
    # 0. if no user, display the workout for the tristan user
    # 0.5. if time of request is after workout has been completed show the alternate
    # 0.75. if time of request is after midnight, show the new workout and add to workout db (steps 1-5)
    # 1. get user (from cookies) -- http://stackoverflow.com/questions/1622793/django-cookies-how-can-i-set-them
    # xxxxx 2. get user log to see what past 7 workouts were xxxxx
    # 3. see if preferences are met
    # xxxxx 4. otherwise, randomly choose from the categories based on preferences xxxxx
    # xxxxx 5. no strength work two consecutive days xxxxx

    global todays_workout

    if request.method == 'POST':
        print(request.id)
    else:
        # temporarily just use tristanlang as all users
        user = User.objects.get_by_natural_key('tristanlang')
        requestdatetime = timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone())

        # check for log with today's date and current user
        listfilter = {'date__gte': requestdatetime.date(), 'user': user}
        todaylog = Log.objects.filter(**listfilter)
        if not todaylog:
            if not todays_workout or todays_workout[0] < requestdatetime.date():
                todays_workout = choose_workout(user, requestdatetime)
            context = {'workout': todays_workout[1]}
        else:
            context = {'log': todaylog[0]}
        
        return render(request, 'workout/workout.html', context)

        

def history(request):
    try:
        history = Log.objects.all().order_by('-date')[:7]
    except:
        history = Log.objects.all().order_by('-date')
    context = {'logs': history}
    return render(request, 'workout/history.html', context)



def new(request):
    context = {'categories': Category.objects.all()}
    return render(request, 'workout/new.html', context)



def preferences(request):
    # temporarily just use tristanlang as all users
    user = User.objects.get_by_natural_key('tristanlang')
    ownerships = Ownership.objects.filter(user=user)
    preferences = Preference.objects.filter(user=user)
    context = {'ownerships': ownerships, 'preferences': preferences}
    return render(request, 'workout/preferences.html', context)