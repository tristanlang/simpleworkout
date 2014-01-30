from django import forms
from django.db.models import Q
from workout.models import Category, Equipment

class WorkoutNotesForm(forms.Form):
    notes = forms.CharField()

class AddNewWorkoutForm(forms.Form):
    category = forms.ModelChoiceField(Category.objects.filter(~Q(category='Rest Day')), empty_label='(Select Workout Category)')
    detail = forms.CharField(widget=forms.Textarea)

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class PreferenceForm(forms.Form):
    cardio_days_per_week = forms.IntegerField()
    circuit_days_per_week = forms.IntegerField()
    strength_days_per_week = forms.IntegerField()

class EquipmentForm(forms.Form):
    equipment = forms.MultipleChoiceField((e, e.item) for e in Equipment.objects.all())