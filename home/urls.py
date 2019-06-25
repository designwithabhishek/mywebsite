from django.contrib import admin
from django.urls import path
from .views import home_list

app_name='home'

urlpatterns = [
    path('', home_list,name="home_list"),
]