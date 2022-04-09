
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from datetime import date, datetime
from .models import Route



now_t=datetime.now().time().strftime("%H:%M")



# def check_date(value):
#     if value<timezone.now().date():
#         print(timezone.now().date())
#
#
#         raise forms.ValidationError("The date must not be in the past")
#     return value
                     


class RouteForm(forms.ModelForm):
    class Meta:
        model=Route

        fields =('departure','destination','date_orig','time_orig', 'time_dep', 'cost', 'no_pass', 'map_pic')
        widgets={'departure':forms.TextInput(attrs={'placeholder': 'Departure','readonly':'readonly','class':'readonly'}),
                 'destination': forms.TextInput(attrs={'placeholder': 'Departure','readonly':'readonly','class':'readonly'}),
                 'date_orig': DateField(attrs={'type': 'date','min':date.today()}),
                 'time_orig':TimeField(attrs={'type': 'time','min':now_t}),
                'time_dep':TimeField(attrs={'type': 'time','min':time_orig}),
                 'cost':FloatField(attrs={'min_value'=0.0, 'error_messages':'min_value': u'Cost cannot be less than 0.0'}),
        'no_pas':forms.IntegerField(min_value=1),
        'map_pic'forms.Charfield(attrs={'type':'hidden'})

        }


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
            raise forms.ValidationError('start time should be later than now.')
        if start > end:
            raise forms.ValidationError({'time_dep':'end time should be later than start time.'})
        return cleaned_data
