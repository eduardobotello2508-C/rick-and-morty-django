from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['name', 'status', 'species', 'type', 'gender', 'image', 'origin', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(choices=[
                ('Alive', 'Alive'),
                ('Dead', 'Dead'),
                ('unknown', 'Unknown')
            ], attrs={'class': 'form-select'}),
            'species': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(choices=[
                ('Female', 'Female'),
                ('Male', 'Male'),
                ('Genderless', 'Genderless'),
                ('unknown', 'Unknown')
            ], attrs={'class': 'form-select'}),
            'image': forms.URLInput(attrs={'class': 'form-control'}),
            'origin': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
        }