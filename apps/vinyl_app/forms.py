from django import forms
from models import Vinyl

class VinylForm(forms.ModelForm):
    class Meta:
        model = Vinyl
        fields = ('title', 'artist', 'description', 'price', 'picture')
