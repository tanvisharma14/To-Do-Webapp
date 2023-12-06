from django.urls import path
from .views import *

urlpatterns = [
    path("addTask/", addTask, name="addTask"),
    path("mark-as-done/<int:pk>/", markAsDone, name="markAsDone"),
    path("mark-as-undone/<int:pk>/", markAsUndone, name="markAsUndone"),
    path("editTask/<int:pk>/", editTask, name="editTask"),
    path("deleteTask/<int:pk>/", deleteTask, name="deleteTask"),
]