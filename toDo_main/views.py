from django.shortcuts import render
from toDo.models import Task

def home(request):
    tasks = Task.objects.filter(isCompleted = False).order_by("-updatedAt")
    return render(request, "home.html", {"tasks": tasks})