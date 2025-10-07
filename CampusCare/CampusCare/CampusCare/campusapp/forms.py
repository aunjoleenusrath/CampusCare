from django import forms
from .models import MedicalService

class MedicalServiceForm(forms.ModelForm):
    class Meta:
        model = MedicalService
        fields = ['name', 'description']
