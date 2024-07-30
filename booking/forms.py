from django import forms
from .models import Trip


class TripForm(forms.ModelForm):
    departure_date = forms.DateField(widget=forms.SelectDateWidget())
    return_date = forms.DateField(widget=forms.SelectDateWidget())

    class Meta:
        model = Trip
        fields = ['id', 'destination', 'departure_date',
                  'return_date', 'number_of_travelers']
