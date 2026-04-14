from django import forms
from .models import Assignment

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['course', 'title', 'description', 'deadline', 'file']
        widgets = {
            'deadline' : forms.DateTimeInput(attrs={'type' : 'datetime-local'})
        }