from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60)
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
    employee_id = models.ForeignKey(Employee,on_delete=CASCADE)

    def save_supervisor(self):
        self.save()

    def delete_supervisor(self):
        self.delete()

    def __str__(self):
        return f"{self.employee_id.first_name} {self.employee_id.middle_name}"