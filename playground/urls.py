from django.contrib import admin  # ✅ Correct
from django.urls import include  # ✅ Correct
from django.urls import path  # ✅ Import path
from . import views

#import views from the current directory
urlpatterns = [
    path('hello/', views.say_hello),
]
