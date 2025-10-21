from django import forms
from .models import MentalSupport

class MentalSupportForm(forms.ModelForm):
    class Meta:
        model = MentalSupport
        fields = ['name', 'description']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter support type'}),
            'Description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Add description...'}),
        }
