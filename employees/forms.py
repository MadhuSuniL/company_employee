from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Employee.objects.all(), widget=forms.Select(attrs={'class': 'select2'}))
    
    class Meta:
        model = Employee
        fields = ['name']
