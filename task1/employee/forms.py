
from dataclasses import field
from django.forms import ModelForm
from .models import empleave_model,status_model
from django import forms
from django.forms.widgets import DateInput # need to import



class empleave_form(ModelForm):
    class Meta:
        model= empleave_model
        fields='__all__'    

        widgets = {
            'from1': DateInput(attrs={'type': 'date'}),
            'to1': DateInput(attrs={'type': 'date'}),
        }


class status_form(ModelForm):
    class Meta:
        model=status_model
        fields='__all__'