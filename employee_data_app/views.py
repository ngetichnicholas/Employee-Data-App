from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.core.exceptions import ObjectDoesNotExist


from .models import *
from .forms import *
from .email import *


# Create your views here.
def index(request):
  current_user = request.user
  employees = Employee.objects.all()
  
  context = {
    'current_user':current_user,
    'employees':employees
    }
  return render(request, 'index.html',context)

def signup_view(request):
    if request.method=='POST':
        signup_form=UserSignUpForm(request.POST)
        if signup_form.is_valid():
            user=signup_form.save()
            user.refresh_from_db()
            return redirect('login')
    else:
        signup_form = UserSignUpForm()
    return render(request, 'registration/signup.html', {'signup_form': signup_form})

@login_required
def profile(request):
  current_user = request.user

  return render(request,'profile/profile.html',{"current_user":current_user})

@login_required
def update_profile(request):
  if request.method == 'POST':
    user_form = UpdateUserForm(request.POST,request.FILES,instance=request.user)
    if user_form.is_valid():
      user_form.save()
      messages.success(request,'Your Profile account has been updated successfully')
      return redirect('profile')
  else:
    user_form = UpdateUserForm(instance=request.user)
  params = {
    'user_form':user_form,
  }
  return render(request,'profile/update.html',params)