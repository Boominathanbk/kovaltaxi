from django import forms

class LocationSearchForm(forms.Form):
    place1 = forms.CharField(label='Place 1', max_length=100)
    place2 = forms.CharField(label='Place 2', max_length=100)
    
    
from django import forms
from datetime import datetime
from .models import Booking

    