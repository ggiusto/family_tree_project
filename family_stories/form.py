# family_stories/forms.py

from django import forms
from .models import FamilyStory

class FamilyStoryForm(forms.ModelForm):
    class Meta:
        model = FamilyStory
        fields = ['title', 'content'] # Autor y fechas se manejan automáticamente
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
        }
        labels = {
            'title': 'Título de la Historia',
            'content': 'Contenido',
        }
