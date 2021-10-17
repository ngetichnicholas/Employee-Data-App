from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import *
from django.forms import Form, ModelForm, DateField, widgets


class UserSignUpForm(UserCreationForm):
    password1 = forms.CharField(label='Enter password', 
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', 
                                widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=("full_name","username","email","password1","password2")
        help_texts = {
            "username":None,
        }

class UpdateUserForm(forms.ModelForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ['username','full_name','email','profile_picture','bio']

class EmployeeForm(forms.ModelForm):
  class Meta:
    model = Employee
    fields = ['first_name','middle_name','graduation_date','employment_date','position','salary','supervisors','employee_code']
    widgets = {
            'graduation_date': widgets.DateInput(attrs={'type': 'date'}),
            'employment_date': widgets.DateInput(attrs={'type': 'date'}),
        }

class SupervisorForm(forms.ModelForm):
  class Meta:
    model = Supervisor
    fields = '__all__'

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ('title','excel_file')