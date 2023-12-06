from django.urls import path
from .views import *

urlpatterns = [
    path("addTask/", addTask, name="addTask")
]