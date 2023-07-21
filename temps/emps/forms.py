from django import forms
from  .models import *

class Blogform(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'