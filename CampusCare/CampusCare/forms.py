from django import forms
from .models import HealthMonitor

class HealthMonitorForm(forms.ModelForm):
    class Meta:
        model = HealthMonitor
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter health service name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe the service...'}),
        }
