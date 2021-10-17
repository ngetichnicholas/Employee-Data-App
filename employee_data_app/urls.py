from django.urls import path
from .import views as app_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',app_views.index,name='index'),
    path('register/',app_views.signup_view,name='register'),
    path('login/',app_views.login,name='login'),
    path('logout/', app_views.custom_logout, name='logout'),
    path('profile/',app_views.profile,name='profile'),
    path('update_profile/',app_views.update_profile,name='update_profile'),

    path('add_employee',app_views.add_employee,name='add_employee'),
    path('employees', app_views.employees,name='employees'),
    path('update_employee/<int:employee_id>', app_views.update_employee,name='update_employee'),
    path('delete_employee/<int:employee_id>', app_views.delete_employee,name='delete_employee'),
    path('employee_details/<int:employee_id>',app_views.employee_details,name='employee_details'),
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)