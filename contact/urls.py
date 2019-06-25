from django.contrib import admin
from django.urls import path
from .views import contacts_list

app_name='contact'

urlpatterns = [
    path('', contacts_list,name="contacts_list"),
]