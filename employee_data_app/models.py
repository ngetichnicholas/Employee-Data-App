from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.core.validators import FileExtensionValidator


# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=144)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to='profiles')

    def save_user(self):
        self.save()

    def delete_user(self):
        self.delete()

    def __str__(self):
        return self.username

class Employee(models.Model):
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60)
    graduation_date = models.DateTimeField()
    employment_date = models.DateTimeField()
    position = models.CharField(max_length=144)
    salary = models.IntegerField()
    supervisors = models.ManyToManyField('Supervisor',blank=True)
    employee_code = models.CharField(max_length=60)

    def save_employee(self):
        self.save()

    def delete_employee(self):
        self.delete()

    def __str__(self):
        return f"{self.first_name} {self.middle_name}"

class Supervisor(models.Model):
    name = models.OneToOneField(Employee,blank=True,on_delete=CASCADE)

    def save_supervisor(self):
        self.save()

    def delete_supervisor(self):
        self.delete()

    def __str__(self):
        return f"{self.name.first_name} {self.name.middle_name}"

class Upload(models.Model):
    title = models.CharField(max_length=144)
    excel_file = models.FileField(upload_to = 'excel/%Y/%m/%d', validators = [FileExtensionValidator(allowed_extensions = ['xlsx'])])
    timestamp = models.DateTimeField(auto_now_add=True)
    records_uploaded = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=20,blank=True,null=True)
    errors = models.CharField(max_length=100,blank=True,null=True)

    def save_upload(self):
        self.save()

    def delete_upload(self):
        self.delete()

    def __str__(self):
        return f"{self.title}"