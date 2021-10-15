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