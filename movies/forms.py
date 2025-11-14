from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = [
            'title',
            'genre',
            'director',
            'release_date',
            'synopsis',
            'picture'
        ]
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'synopsis': forms.Textarea(attrs={'rows': 4}),
        }
