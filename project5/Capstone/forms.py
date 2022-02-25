
from django import forms
import datetime

class RouteForm(forms.Form):
    departure = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Departure'}))
    destination = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Destination'}))
    date_orig=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    time_orig=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    time_dep=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    cost=forms.FloatField()
    no_pass = forms.IntegerField()