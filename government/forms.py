from django.contrib.auth.forms import UserCreationForm
from django import forms


from customuser.models import CustomUser, College


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']


class CollegeRegistrationForm(forms.ModelForm):
    class Meta:
        model = College
        fields = ['college_name']
