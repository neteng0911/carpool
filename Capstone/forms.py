
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from datetime import date, datetime
from .models import Route, User
from django.utils.timezone import make_aware



now_t=datetime.now().time().strftime("%H:%M")


                     


class RouteForm(forms.ModelForm):
    error_css_class='error_field'
    required_css_class = 'required-field'


    departure = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Departure','readonly':'readonly','class':'readonly'}))
    destination = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Destination','readonly':'readonly','class':'readonly'}))
    date_orig=forms.DateField(widget=forms.DateInput(attrs={'type': 'date','min':date.today(),'format':['%y-%m-%d']}))

    time_orig=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    time_dep=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time','min':time_orig}))

    cost=forms.FloatField(min_value=0.0,error_messages={'min_value': u'Cost cannot be less than 0.0'})
    no_pass = forms.IntegerField(min_value=1, label='Passengers')
    map_pic=forms.CharField(widget=forms.HiddenInput())
    dist = forms.FloatField(widget=forms.HiddenInput())
    #d_a = forms.BooleanField(label='Disabled access',help_text='Check if at least one disabled passenger can join',required=False)


    class Meta:
        model = Route
        fields = ['departure','destination','date_orig','time_orig', 'time_dep', 'cost', 'no_pass', 'map_pic','dist']
        # help_texts = {
        #     'd_a': ('Check if at least one disabled passenger can join'),
        # }
        # labels ={'d_a':'Disabled access'}
#validators regarding date and time

    def clean(self):
        cleaned_data = super().clean()
        date_inp=cleaned_data.get('date_orig')
        start = cleaned_data.get('time_orig')
        end = cleaned_data.get('time_dep')
        #print(date_inp)
        #print(date.today())
        #print(start)
        #print(end)

        if date_inp <date.today():
            raise forms.ValidationError({'date_orig':'start date should be later than today.'})

        if date_inp == date.today() and start < datetime.now().time():
            raise forms.ValidationError('start time should be later than now.')
        if start > end:
            raise forms.ValidationError({'time_dep':'end time should be later than start time.'})
        return cleaned_data

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['profile_pic', 'about']


