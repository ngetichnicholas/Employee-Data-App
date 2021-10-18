from django.contrib.auth import login, authenticate, logout
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.core.exceptions import ObjectDoesNotExist

import openpyxl
import random

from .models import *
from .forms import *
from .email import *

# Create your views here.


def index(request):
    current_user = request.user
    employees = Employee.objects.all()

    context = {
        'current_user': current_user,
        'employees': employees
    }
    return render(request, 'index.html', context)


def signup_view(request):
    if request.method == 'POST':
        signup_form = UserSignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            user.refresh_from_db()
            return redirect('login')
    else:
        signup_form = UserSignUpForm()
    return render(request, 'registration/signup.html', {'signup_form': signup_form})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('index')

            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"form": form})


def custom_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')


# Generate 3 digits random number
def rand_3_digit_num():
    random_digits = random.randint(10**(3-1), 10**3-1)
    return random_digits


@login_required
def add_employee(request):
    if request.method == 'POST':
        add_employee_form = EmployeeForm(request.POST, request.FILES)
        if add_employee_form.is_valid():
            employee = add_employee_form.save(commit=False)

            # Get first name initial letter
            initial_letter = employee.first_name[0]
            print(f'Initial letter:{initial_letter}')

            # Get middle name initial letter
            last_letter = employee.middle_name[0]
            print(f'Last letter: {last_letter}')

            random_number = rand_3_digit_num()

            # Join initial letter,random number and last letter
            code = (initial_letter+str(random_number)+last_letter)
            print(code)
            employee.employee_code = code
            employee.save()
            messages.success(request, f'New employee added!')
            return redirect('index')

    else:
        add_employee_form = EmployeeForm()

    return render(request, 'employees/add_employee.html', {'add_employee_form': add_employee_form})


@login_required
def add_supervisor(request):
    if request.method == 'POST':
        add_supervisor_form = SupervisorForm(request.POST, request.FILES)
        if add_supervisor_form.is_valid():
            supervisor = add_supervisor_form.save(commit=False)
            supervisor.save()
            messages.success(request, f'New supervisor added!')
            return redirect('index')

    else:
        add_supervisor_form = SupervisorForm()

    return render(request, 'add_supervisor.html', {'add_supervisor_form': add_supervisor_form})


@login_required
def employees(request):
    employees = Employee.objects.all().order_by('-employee_code')
    return render(request, 'employees/employees.html', {'employees': employees})


def employee_details(request, employee_id):
    current_user = request.user
    employee = Employee.objects.get(pk=employee_id)

    return render(request, 'employees/employee_page.html', {'current_user': current_user, 'employee': employee})


@login_required
def update_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)

    if request.method == 'POST':
        update_employee_form = EmployeeForm(
            request.POST, request.FILES, instance=employee)
        if update_employee_form.is_valid():
            update_employee_form.save()
            messages.success(request, f'employee updated!')
            return redirect('employees')
    else:
        update_employee_form = EmployeeForm(instance=employee)
    context = {
        "update_employee_form": update_employee_form,
        "employee": employee
    }
    return render(request, 'employees/update_employee.html', context)


@login_required
def delete_employee(request, employee_id):
    employee = Employee.objects.get(pk=employee_id)
    if employee:
        employee.delete_employee()
        messages.success(request, f'employee deleted!')
    return redirect('employees')


# Uploads display view
def uploads(request):
    uploads = Upload.objects.all()
    return render(request, 'uploads/uploads.html', {'uploads': uploads})


# Get single upload details
def upload_details(request, upload_id):
    current_user = request.user
    upload = Upload.objects.get(pk=upload_id)

    return render(request, 'uploads/upload_page.html', {'current_user': current_user, 'upload': upload})


# Update upload
@login_required
def update_upload(request, upload_id):
    upload = Upload.objects.get(pk=upload_id)

    if request.method == 'POST':
        update_upload_form = UploadFileForm(
            request.POST, request.FILES, instance=upload)
        if update_upload_form.is_valid():
            update_upload_form.save()
            messages.success(request, f'Upload updated!')
            return redirect('uploads')
    else:
        update_upload_form = UploadFileForm(instance=upload)
    context = {
        "update_upload_form": update_upload_form,
        "upload": upload
    }
    return render(request, 'uploads/update_upload.html', context)


# Delete upload
@login_required
def delete_upload(request, upload_id):
    upload = Upload.objects.get(pk=upload_id)
    if upload:
        upload.delete_upload()
        messages.success(request, f'Upload deleted!')
    return redirect('uploads')


# Add new upload
def add_upload(request):
    if request.method == 'POST':
        excel_file = request.FILES["excel_file"]

        upload_form = UploadFileForm(request.POST, request.FILES)

        if upload_form.is_valid():
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.worksheets[0]
            row_count = sheet.max_row
            upload = upload_form.save(commit=False)
            upload.records_uploaded = row_count
            upload.status = 'Complete'
            upload.errors = 'None'
            upload.save()
            messages.success(request, "Excel file uploaded successfully")
            return redirect('index')
    else:
        upload_form = UploadFileForm()
    return render(request, 'uploads/upload_excel.html', {'upload_form': upload_form})


@login_required
def profile(request):
    current_user = request.user

    return render(request, 'profile/profile.html', {"current_user": current_user})


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(
            request.POST, request.FILES, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(
                request, 'Your Profile account has been updated successfully')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
    params = {
        'user_form': user_form,
    }
    return render(request, 'profile/update.html', params)
