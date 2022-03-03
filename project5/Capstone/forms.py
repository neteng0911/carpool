
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime,date


# def check_date(value):
#     if value<timezone.now().date():
#         print(timezone.now().date())
#
#
#         raise forms.ValidationError("The date must not be in the past")
#     return value
                     


class RouteForm(forms.Form):
    departure = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Departure'}))
    destination = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Destination'}))
    date_orig=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    #date_orig=forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), validators=[check_date])
    time_orig=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    time_dep=forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    cost=forms.FloatField(min_value=0.0,error_messages={'min_value': u'Cost cannot be less than 0.0'})
    no_pass = forms.IntegerField(min_value=1)



    def clean(self):
        cleaned_data = super().clean()
        date_inp=cleaned_data.get('date_orig')
        start = cleaned_data.get('time_orig')
        end = cleaned_data.get('time_dep')
        print(date_inp)
        print(date.today())
        print(start)
        print(end)

        if date_inp <date.today():
            raise forms.ValidationError({'date_orig':'start date should be later than today.'})

        if start<datetime.now().time():
            raise forms.ValidationError('start time should later than now.')
        if start > end:
            raise forms.ValidationError('end time should later start time.')
        return cleaned_data