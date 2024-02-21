# myapp/urls.py
from django.urls import path 
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),
    path('company/', views.company, name='company'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('submit_report/', views.submit_report, name='submit_report'),
   ]
