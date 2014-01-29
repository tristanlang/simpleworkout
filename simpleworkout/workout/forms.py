from django import forms
from django.db.models import Q
from workout.models import Category

class WorkoutNotesForm(forms.Form):
    notes = forms.CharField()

class AddNewWorkoutForm(forms.Form):
    category = forms.ModelChoiceField(Category.objects.filter(~Q(category='Rest Day')), empty_label='(Select Workout Category)')
    detail = forms.CharField()