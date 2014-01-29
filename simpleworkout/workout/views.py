from django.shortcuts import render
from django.views import generic
import random
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

from workout.models import Log, Workout, Category, Ownership, Preference
from workout.forms import WorkoutNotesForm, AddNewWorkoutForm

# signup view
# login view

todays_workout = None

def weight_first_category(category1, category2):
    if random.randint(0,2):
        return random.choice(Workout.objects.filter('category' == category1))
    else:
        return random.choice(Workout.objects.filter('category' == category2))

def choose_workout(user, requestdate):
    today = requestdate
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
            workout = random.choice((random.choice(Workout.objects.filter(category=strength)),
                random.choice(Workout.objects.filter(category=circuit))))
    else:
        workout = random.choice(Workout.objects.filter(category=cardio))
    return (today, workout)



def about(request):
    return render(request, 'workout/about.html')



def workout(request):
    global todays_workout

    # temporarily just use tristan as all users
    user = User.objects.get_by_natural_key('tristan')
    requestdate = timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone()).date()

    if request.method == 'POST':
        rest = request.POST.get('rest')
        completed = request.POST.get('completed')
        noted = request.POST.get('noted')

        if completed:
            if todays_workout and todays_workout[0] >= requestdate:
                context = {'workout': todays_workout[1], 'addnotes': True}
                return render(request, 'workout/workout.html', context)

        if rest:
            restday = Workout.objects.get(detail='Rest Day')
            log = Log(user=user, workout=workout, date=requestdate)
            log.save()
            context = {'log': log}
            return render(request, 'workout/workout.html', context)

        if noted:
            form = WorkoutNotesForm(request.POST)
            if form.is_valid():
                notes = form.cleaned_data['notes']
                log = Log(user=user, workout=todays_workout[1], date=requestdate, notes=notes)
                log.save()
                todays_workout = None
                context = {'log': log}
                return render(request, 'workout/workout.html', context)

    else: # GET
        # check for log with today's date and current user
        listfilter = {'date__gte': requestdate, 'user': user}
        todaylog = Log.objects.filter(**listfilter)
        if not todaylog:
            if not todays_workout or todays_workout[0] < requestdate:
                todays_workout = choose_workout(user, requestdate)
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
    if request.method == 'POST':
        return None
    else:
        form = AddNewWorkoutForm()
        #context = {'categories': Category.objects.all()}
        context = {'form': form}
        return render(request, 'workout/new.html', context)



def preferences(request):
    # temporarily just use tristanlang as all users
    user = User.objects.get_by_natural_key('tristanlang')
    ownerships = Ownership.objects.filter(user=user)
    preferences = Preference.objects.filter(user=user)
    context = {'ownerships': ownerships, 'preferences': preferences}
    return render(request, 'workout/preferences.html', context)