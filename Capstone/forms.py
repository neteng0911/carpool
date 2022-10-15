
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from datetime import date, datetime
from .models import Route, User
from django.utils.timezone import make_aware
from django.utils.translation import gettext_lazy as _



now_t=datetime.now().time().strftime("%H:%M")





class RouteForm(forms.ModelForm):
    error_css_class='error_field'
    required_css_class = 'required-field'


    departure = forms.CharField(label=_('Departure'),
         widget=forms.TextInput(attrs={'readonly':'readonly','class':'readonly'}))
    destination = forms.CharField(label=_('Destination'),
        widget=forms.TextInput(attrs={'readonly':'readonly','class':'readonly'}))
    date_orig=forms.DateField(label=_('Date of departure'),widget=forms.DateInput(attrs={'type': 'date','min':date.today(),'format':['%y-%m-%d']}))

    time_orig=forms.TimeField(widget=forms.TimeInput(attrs={'label':_('Time of departure'), 'type': 'time'}))
    date_ret = forms.DateField(
        widget=forms.DateInput(attrs={'label':_('Date_of return'),'type': 'date', 'min': date_orig, 'format': ['%y-%m-%d']}))
    time_dep=forms.TimeField(widget=forms.TimeInput(attrs={'label':_('Time of departure'),'type': 'time','min':time_orig}))

    cost=forms.FloatField(label=_('cost'),min_value=0.0,error_messages={'min_value': u'Cost cannot be less than 0.0'})
    no_pass = forms.IntegerField(min_value=1, label=_('Passengers'))
    map_pic=forms.CharField(widget=forms.HiddenInput())
    dist = forms.FloatField(widget=forms.HiddenInput())
    d_a = forms.BooleanField(label=_('Disabled access'),help_text=_('Check if at least one disabled passenger can join'),required=False,
                             initial=False)



    class Meta:
        model = Route
        fields = ['departure','destination','date_orig','time_orig','date_ret', 'time_dep', 'cost', 'no_pass', 'map_pic','dist']


    def clean(self):
        cleaned_data = super().clean()
        date_inp=cleaned_data.get('date_orig')
        date_inp_ret = cleaned_data.get('date_ret')
        start = cleaned_data.get('time_orig')
        end = cleaned_data.get('time_dep')
        #print(date_inp)
        #print(date.today())
        #print(start)
        #print(end)

        if date_inp <date.today():
            raise forms.ValidationError({'date_orig':'start date should be later than today.'})
        if date_inp_ret <date_inp:
            raise forms.ValidationError({'date_ret':'return date should be later than start date.'})
        if date_inp == date.today() and start < datetime.now().time():
            raise forms.ValidationError('start time should be later than now.')
        if date_inp_ret  == date_inp and start > end:
            raise forms.ValidationError({'time_dep':'end time should be later than start time.'})
        return cleaned_data

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['profile_pic', 'about']


