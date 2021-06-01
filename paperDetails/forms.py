from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Faculty


class FacultyInfoUpdateForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = ['name', 'email', 'empId']
