from django import forms
from ..models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['nip','name', 'email', 'photo', 'total_project']
        labels = {
            'nip': 'NIP',
            'name': 'Name',
            'email': 'Email',
            'photo': 'Photo',
            'total_project': 'Total Project',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'input'}),
            'total_project': forms.NumberInput(attrs={'class': 'input'}),
        }