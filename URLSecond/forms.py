from django import forms
from .models import UrlShortener

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlShortener
        fields = ['long_url']
