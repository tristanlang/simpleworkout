from django.shortcuts import render, redirect
from django.views import generic
import random
from django.contrib.auth.views import password_change, password_change_done
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.utils import timezone
import datetime

from workout.models import Log, Workout, Category, Ownership, Preference, Equipment
from workout.forms import WorkoutNotesForm, AddNewWorkoutForm, LoginForm, PreferenceForm, EquipmentForm



todays_workout = {}

def weight_first_category(category1, category2):
    if random.randint(0,2):
        return random.choice(Workout.objects.filter(category=category1))
    else:
        return random.choice(Workout.objects.filter(category=category2))

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
    if request.user.is_anonymous(): user = User.objects.get_by_natural_key('tristan')
    else: user = request.user
    requestdate = timezone.make_aware(datetime.datetime.now(),timezone.get_default_timezone()).date()

    if request.method == 'POST':
        if request.user.is_anonymous():
            context = {'workout': todays_workout[user][1], 'submiterror': True}
            return render(request, 'workout/workout.html', context)

        # see which button was clicked
        rest = request.POST.get('rest')
        completed = request.POST.get('completed')
        noted = request.POST.get('noted')

        if completed:
            if user in todays_workout and todays_workout[user][0] >= requestdate:
                context = {'workout': todays_workout[user][1], 'addnotes': True}
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
                log = Log(user=user, workout=todays_workout[user][1], date=requestdate, notes=notes)
                log.save()
                todays_workout[user] = None
                context = {'log': log}
                return render(request, 'workout/workout.html', context)
    else:
        # check for log with today's date and current user
        listfilter = {'date__gte': requestdate, 'user': user}
        todaylog = Log.objects.filter(**listfilter)
        if not todaylog:
            if user not in todays_workout or todays_workout[user][0] < requestdate:
                todays_workout[user] = choose_workout(user, requestdate)
            context = {'workout': todays_workout[user][1]}
        else:
            context = {'log': todaylog[0]}
        return render(request, 'workout/workout.html', context)

        

def history(request):
    if request.user.is_anonymous(): user = User.objects.get_by_natural_key('tristan')
    else: user = request.user
    logs = Log.objects.filter(user=user)

    try:
        history = logs.order_by('-date')[:7]
    except:
        history = logs.order_by('-date')
    context = {'logs': history}
    return render(request, 'workout/history.html', context)



def new(request):
    if request.method == 'POST':
        print(request.user)
        form = AddNewWorkoutForm(request.POST)
        if form.is_valid():
            if request.user.is_anonymous():
                context = {'anonerror': True, 'form': form}
                return render(request, 'workout/new.html', context)
            else:
                workout = Workout(category=form.cleaned_data['category'], 
                    detail=form.cleaned_data['detail'])
                workout.save()
                context = {'workout': workout}
                return render(request, 'workout/added.html', context)
    else:
        form = AddNewWorkoutForm()
        context = {'form': form}
        return render(request, 'workout/new.html', context)



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
                user = authenticate(username=form.cleaned_data['username'], 
                    password = form.cleaned_data['password'])
                
                if user is not None and user.is_active:
                    login(request, user)
                    newurl = request.GET.get('next')
                    return redirect(newurl)
                else:
                    context = {'form': form, 'loginerror': True}
                    return render(request, 'workout/login.html', context)
    else:
        form = LoginForm()
        context = {'form': form}
        return render(request, 'workout/login.html', context)



def logout_view(request):
    logout(request)
    newurl = request.GET.get('next')
    return redirect(newurl)



def preferences(request):
    if request.user.is_anonymous(): user = User.objects.get_by_natural_key('tristan')
    else: user = request.user

    if request.method == 'POST':
        equipment_form = EquipmentForm(request.POST)
        preference_form = PreferenceForm(request.POST)

        # check for real user
        if request.user.is_anonymous():
            context = {'anonerror': True, 'equipment_form': equipment_form, 'preference_form': preference_form}
            return render(request, 'workout/preferences.html', context)
        else:
            if equipment_form.is_valid():
                updated_equipment = set(Equipment.objects.get(item=item) for item in equipment_form.cleaned_data['equipment'])
                current_equipment = set(owner.equipment for owner in Ownership.objects.filter(user=user))

                # look through current_equipment for the equipment the user did not select and delete those
                for item in current_equipment:
                    if item not in updated_equipment:
                        Ownership.objects.get(equipment=item, user=user).delete()

                # look through updated_equipment for the equipment the user does not currently have and add those
                for item in updated_equipment:
                    if item not in current_equipment:
                        newequip = Ownership(user=user, equipment=item)
                        newequip.save()

            if preference_form.is_valid():
                # make sure days are in appropriate ranges and formats, otherwise re-render with an error
                try:
                    cardiodays = int(preference_form.cleaned_data['cardio_days_per_week'])
                    circuitdays = int(preference_form.cleaned_data['circuit_days_per_week'])
                    strengthdays = int(preference_form.cleaned_data['strength_days_per_week'])
                except:
                    context = {'equipment_form': equipment_form, 'preference_form': preference_form, 'dayserror': True}
                    return render(request, 'workout/preferences.html', context)
                
                if not (0 <= cardiodays <= 7) or not (0 <= circuitdays <= 7) or not (0 <= strengthdays <= 7) or not sum([cardiodays, circuitdays, strengthdays])==7:
                    context = {'equipment_form': equipment_form, 'preference_form': preference_form, 'dayserror': True}
                    return render(request, 'workout/preferences.html', context)

                # try modifying user's preferences, otherwise create one
                try:
                    pcardio = Preference.objects.get(user=user, category=Category.objects.get(category='Cardio'))
                    pcardio.days_per_week = cardiodays
                except:
                    pcardio = Preference(user=user, category=Category.objects.get(category='Cardio'), days_per_week=cardiodays)
                pcardio.save()

                # try modifying user's preferences, otherwise create one
                try: 
                    pcircuit = Preference.objects.get(user=user, category=Category.objects.get(category='Circuit'))
                    pcircuit.days_per_week = circuitdays
                except:
                    pcircuit = Preference(user=user, category=Category.objects.get(category='Circuit'), days_per_week=circuitdays)
                pcircuit.save()

                # try modifying user's preferences, otherwise create one
                try: 
                    pstrength = Preference.objects.get(user=user, category=Category.objects.get(category='Strength'))
                    pstrength.days_per_week = strengthdays
                except:
                    pstrength = Preference(user=user, category=Category.objects.get(category='Strength'), days_per_week=strengthdays)
                pstrength.save()

            print(Ownership.objects.filter(user=user))
            context = {'preferences': Preference.objects.filter(user=user), 
                    'ownership': Ownership.objects.filter(user=user), 'user': user}
            return render(request, 'workout/added.html', context)
    else:
        # get current days_per_week for each category
        try: cardiodays = Preference.objects.get(user=user, category=Category.objects.get(category='Cardio')).days_per_week
        except: cardiodays = 0

        try: circuitdays = Preference.objects.get(user=user, category=Category.objects.get(category='Circuit')).days_per_week
        except: circuitdays = 0

        try: strengthdays = Preference.objects.get(user=user, category=Category.objects.get(category='Strength')).days_per_week
        except: strengthdays = 0

        # get current equipment owned
        try: owned = dict((o.equipment, o.equipment.item) for o in Ownership.objects.filter(user=user))
        except: owned = {}

        # pre-populate forms
        preference_form = PreferenceForm({'cardio_days_per_week': cardiodays, 'circuit_days_per_week': circuitdays, 'strength_days_per_week': strengthdays})
        equipment_form = EquipmentForm()
        equipment_form.fields['equipment'].initial = owned
       
        context = {'equipment_form': equipment_form, 'preference_form': preference_form}
        return render(request, 'workout/preferences.html', context)

def cust_password_change(request):
    return password_change(request, template_name='registration/password_change.html', post_change_redirect='/workout/password_change/done/')

def cust_password_change_done(request):
    return password_change_done(request, template_name='registration/password_changed.html')