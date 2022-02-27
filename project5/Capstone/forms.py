
from django import forms
from datetime import datetime
def the_date():
    return datetime(year=datetime.today.year,month=datetime.today.month,day=datetime.today.day+1)
class RouteForm(forms.Form):
    departure = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Departure'}))
    destination = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Destination'}))
    date_orig=forms.DateTimeField(initial=the_date,widget=forms.DateTimeInput(attrs={'type': 'date'}))
    time_orig=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    time_dep=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    cost=forms.FloatField()
    no_pass = forms.IntegerField()