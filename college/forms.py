from django import forms
from customuser.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['registration_no', 'name', 'other_details']