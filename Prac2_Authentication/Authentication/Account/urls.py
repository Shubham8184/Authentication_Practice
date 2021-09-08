from django.urls import path
from .views import *



urlpatterns=[
    path('home/',Homeview,name='home'),
    path('login/',Loginuserview,name='login'),
    path('register/',Registeruserview,name='register'),
    path('logout/',Logoutview,name='logout'),
]