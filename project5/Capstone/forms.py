
from django import forms
import datetime

class RouteForm(forms.Form):
    origin = forms.CharField(label='Origin', max_length=64)
    destination = forms.CharField(label='Destination', max_length=64)
    date_orig=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    time_orig=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    time_dep=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    cost=forms.FloatField()
    no_pass = forms.IntegerField()