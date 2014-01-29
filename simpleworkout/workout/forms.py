from django import forms

class NotesForm(forms.Form):
    notes = forms.CharField()