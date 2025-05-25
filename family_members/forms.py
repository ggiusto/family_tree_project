# family_members/forms.py

from django import forms
from .models import FamilyMember

class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'relationship': forms.Select(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        labels = {
            'first_name': 'Nombre', 'last_name': 'Apellido', 'relationship': 'Relación',
            'birth_date': 'Fecha de Nacimiento', 'email': 'Correo Electrónico',
            'phone_number': 'Número de Teléfono', 'address': 'Dirección',
        }
