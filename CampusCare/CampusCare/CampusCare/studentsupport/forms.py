from django import forms
from .models import StudentSupport

class StudentSupportForm(forms.ModelForm):
    class Meta:
        model = StudentSupport
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter support category'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe the support...'}),
        }
