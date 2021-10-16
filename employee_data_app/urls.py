from django.urls import path
from .import views as app_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',app_views.index,name='index'),
    path('register/',app_views.signup_view,name='register'),
    path('login/',app_views.login,name='login'),
    path('profile/',app_views.profile,name='profile'),
    path('update_profile/',app_views.update_profile,name='update_profile'),

]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)