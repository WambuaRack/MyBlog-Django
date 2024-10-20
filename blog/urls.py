from django.urls import path
from django.contrib import admin  # Import the admin module
from .views import post_list, post_create  # Import your views

urlpatterns = [
    path('', post_list, name='post_list'),  # Main post list
    path('create/', post_create, name='post_create'),  # Post creation
]
