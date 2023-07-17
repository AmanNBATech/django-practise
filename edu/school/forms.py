from django import forms
from  .models import *


class vehcileform(forms.ModelForm):
    class Meta:
        model=vehcile
        fields='__all__'


class sportsform(forms.ModelForm):
    class Meta:
        model=sports
        fields='__all__'
 