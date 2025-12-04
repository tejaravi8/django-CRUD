from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border w-full px-3 py-2 rounded'}),
            'age': forms.NumberInput(attrs={'class': 'border w-full px-3 py-2 rounded'}),
            'email': forms.EmailInput(attrs={'class': 'border w-full px-3 py-2 rounded'}),
        }