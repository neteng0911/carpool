
from django import forms
import datetime

class RouteForm(forms.Form):
    origin = forms.CharField(label='Origin', max_length=100)
    dest = forms.CharField(label='Destination', max_length=100)
    date_orig=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    time_orig=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    date_dep=forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'date'}))
    time_dep=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    num_passengers=forms.IntegerField()
    cost=forms.FloatField()